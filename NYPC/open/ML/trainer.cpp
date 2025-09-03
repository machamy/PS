// trainer.cpp
// Yacht Auction — PBT self-play trainer (C++)
// - Focus: Learning bidding policy parameters via population-based training
// - Scoring phase reuses rule-based bestImmediatePick from the sample
// - Outputs data.bin: a bank of top agents (champion + alternates)
// Build: g++ -O3 -std=c++17 -o trainer trainer.cpp
// Run:   ./trainer
#include <bits/stdc++.h>
using namespace std;

// ======== Game constants (match sample) ========
static const double  ALPHA_SELF_BASE_DEF    = 0.95;
static const int     DELTA_AVOID_DEF        = 1500;
static const int     SMALL_DELTA_ZERO_DEF   = 1200;
static const int     COLLISION_CAP_DEF      = 6000;
static const int     NONCOLLISION_CAP_DEF   = 12000;
static const double  ROI_MAX_RATIO_DEF      = 1.00;
static const int     ZERO_BID_PERIOD_DEF    = 23;
static const int     ZERO_BID_PHASE_DEF     = 7;
static const int     BANKROLL_CAP_DEF       = 75000;
static const double  BANKROLL_ALPHA_SCL_DEF = 0.80;
static const int     HEDGE_MARGIN_MIN_DEF   = 400;
static const int     HEDGE_MARGIN_MAX_DEF   = 900;

enum Cat { ONE, TWO, THREE, FOUR, FIVE, SIX,
           CHOICE, FOUR_OF_A_KIND, FULL_HOUSE, SMALL_STRAIGHT, LARGE_STRAIGHT, YACHT,
           CAT_CNT };

using Cnt = array<int,7>; // 1..6

inline Cnt zeroCnt(){ Cnt c{}; return c; }
inline int diceCount(const Cnt& c){ int s=0; for(int f=1;f<=6;++f) s+=c[f]; return s; }
inline Cnt toCnt(const vector<int>& v){ Cnt c{}; for(int x: v) ++c[x]; return c; }
inline Cnt addCnt(Cnt a, const Cnt& b){ for(int f=1;f<=6;++f) a[f]+=b[f]; return a; }
inline Cnt subCnt(Cnt a, const Cnt& b){ for(int f=1;f<=6;++f) a[f]-=b[f]; return a; }
inline vector<int> expandCnt(const Cnt& c){ vector<int> v; for(int f=1;f<=6;++f) for(int k=0;k<c[f];++k) v.push_back(f); return v; }
inline int sumDice(const Cnt& c){ int s=0; for(int f=1;f<=6;++f) s+=f*c[f]; return s; }
inline double clampd(double x, double a, double b){ return x<a?a:(x>b?b:x); }
inline int clampiLL(long long x, int lo, int hi){ if(x<lo) return lo; if(x>hi) return hi; return (int)x; }
inline uint32_t facesMask(const Cnt& c){ uint32_t m=0; for(int f=1;f<=6;++f) if(c[f]>0) m|=(1u<<(f-1)); return m; }
static Cnt pickSmallest(const Cnt& c, int need){ Cnt t{}; int left=need; for(int f=1;f<=6&&left>0;++f){int k=min(c[f],left); t[f]=k; left-=k;} return t; }
static Cnt pickLargest(const Cnt& c, int need){ Cnt t{}; int left=need; for(int f=6;f>=1&&left>0;--f){int k=min(c[f],left); t[f]=k; left-=k;} return t; }

// ======== Immediate scoring (same as sample, condensed) ========
static inline int scoreUpperOnly(const Cnt& all, int face){ int use=min(all[face],5); return use*face*1000; }
static inline int scoreChoiceOnly(const Cnt& all){ int need=5, s=0; for(int f=6; f>=1 && need>0; --f){ int t=min(all[f],need); s+=t*f; need-=t; } return s*1000; }
static inline int scoreFourKindOnly(const Cnt& all){
    int best=0; for(int f=1;f<=6;++f) if(all[f]>=4){
        int s=4*f; for(int g=6; g>=1; --g){ if(g==f) continue; if(all[g]>0){ s+=g; break; } } best=max(best, s*1000);
    } return best;
}
static inline int scoreFullHouseOnly(const Cnt& all){
    int best=0;
    for(int a=1;a<=6;++a) if(all[a]>=3){
        for(int b=1;b<=6;++b){ if(b==a) continue; if(all[b]>=2){ best=max(best,(3*a+2*b)*1000); }}
        if(all[a]>=5) best=max(best,5*a*1000);
    } return best;
}
static inline int scoreSmallStraightOnly(uint32_t m){
    return ((m&0x0F)==0x0F || (m&0x1E)==0x1E || (m&0x3C)==0x3C) ? 15000 : 0;
}
static inline int scoreLargeStraightOnly(uint32_t m){
    return (((m&0x1F)==0x1F)||((m&0x3E)==0x3E)) ? 30000 : 0;
}
static inline int scoreYachtOnly(const Cnt& all){ for(int f=1;f<=6;++f) if(all[f]>=5) return 50000; return 0; }

static int bestImmediateScore(const Cnt& all, int remMask){
    uint32_t m = facesMask(all);
    int best=0;
    if(remMask&(1<<ONE))   best=max(best,scoreUpperOnly(all,1));
    if(remMask&(1<<TWO))   best=max(best,scoreUpperOnly(all,2));
    if(remMask&(1<<THREE)) best=max(best,scoreUpperOnly(all,3));
    if(remMask&(1<<FOUR))  best=max(best,scoreUpperOnly(all,4));
    if(remMask&(1<<FIVE))  best=max(best,scoreUpperOnly(all,5));
    if(remMask&(1<<SIX))   best=max(best,scoreUpperOnly(all,6));
    if(remMask&(1<<CHOICE)) best=max(best,scoreChoiceOnly(all));
    if(remMask&(1<<FOUR_OF_A_KIND)) best=max(best,scoreFourKindOnly(all));
    if(remMask&(1<<FULL_HOUSE))     best=max(best,scoreFullHouseOnly(all));
    if(remMask&(1<<SMALL_STRAIGHT)) best=max(best,scoreSmallStraightOnly(m));
    if(remMask&(1<<LARGE_STRAIGHT)) best=max(best,scoreLargeStraightOnly(m));
    if(remMask&(1<<YACHT))          best=max(best,scoreYachtOnly(all));
    return best;
}

// Build used dice for each category (same spirit as sample; minimal)
static Cnt buildUsedUpper(const Cnt& all, int face){ Cnt u{}; int t=min(all[face],5); u[face]=t; int need=5-t; if(need>0){ Cnt rest=all; rest[face]-=t; Cnt ex=pickSmallest(rest,need); for(int f=1;f<=6;++f) u[f]+=ex[f]; } return u; }
static pair<int,Cnt> scoreUpper(const Cnt& all, int face){ Cnt u=buildUsedUpper(all,face); return {u[face]*face*1000,u}; }
static pair<int,Cnt> scoreChoice(const Cnt& all){ Cnt u=pickLargest(all,5); int s=0; for(int f=1;f<=6;++f) s+=f*u[f]; return {s*1000,u}; }
static pair<int,Cnt> scoreFourKind(const Cnt& all){ int best=-1; Cnt bu{}; for(int f=1;f<=6;++f) if(all[f]>=4){ Cnt u{}; u[f]=4; Cnt rest=subCnt(all,u); Cnt ex=pickLargest(rest,1); for(int k=1;k<=6;++k) u[k]+=ex[k]; int s=0; for(int k=1;k<=6;++k) s+=k*u[k]; s*=1000; if(s>best){best=s; bu=u;} } if(best<0) return {0,pickSmallest(all,5)}; return {best,bu}; }
static pair<int,Cnt> scoreFullHouse(const Cnt& all){ int best=-1; Cnt bu{}; for(int a=1;a<=6;++a){ if(all[a]>=3){ for(int b=1;b<=6;++b){ if(a==b) continue; if(all[b]>=2){ Cnt u{}; u[a]=3; u[b]=2; int s=(3*a+2*b)*1000; if(s>best){best=s; bu=u;} } } if(all[a]>=5){ Cnt u{}; u[a]=5; int s=5*a*1000; if(s>best){best=s; bu=u;} } } } if(best<0) return {0,pickSmallest(all,5)}; return {best,bu}; }
static pair<int,Cnt> scoreSmallStraight(const Cnt& all){ uint32_t m=facesMask(all); if(((m&0x0F)==0x0F)||((m&0x1E)==0x1E)||((m&0x3C)==0x3C)){ Cnt u{}; if((m&0x0F)==0x0F){ u[1]=u[2]=u[3]=u[4]=1; } else if((m&0x1E)==0x1E){ u[2]=u[3]=u[4]=u[5]=1; } else { u[3]=u[4]=u[5]=u[6]=1; } Cnt rest=subCnt(all,u); Cnt ex=pickSmallest(rest,1); for(int f=1;f<=6;++f) u[f]+=ex[f]; return {15000,u}; } return {0,pickSmallest(all,5)}; }
static pair<int,Cnt> scoreLargeStraight(const Cnt& all){ uint32_t m=facesMask(all); if(((m&0x1F)==0x1F)||((m&0x3E)==0x3E)){ Cnt u{}; if((m&0x1F)==0x1F){ u[1]=u[2]=u[3]=u[4]=u[5]=1; } else { u[2]=u[3]=u[4]=u[5]=u[6]=1; } return {30000,u}; } return {0,pickSmallest(all,5)}; }
static pair<int,Cnt> scoreYacht(const Cnt& all){ for(int f=1;f<=6;++f) if(all[f]>=5){ Cnt u{}; u[f]=5; return {50000,u}; } return {0,pickSmallest(all,5)}; }

static pair<int,Cnt> scoreByCat(const Cnt& all, Cat c){
    switch(c){
        case ONE: return scoreUpper(all,1); case TWO: return scoreUpper(all,2);
        case THREE:return scoreUpper(all,3); case FOUR: return scoreUpper(all,4);
        case FIVE: return scoreUpper(all,5); case SIX:  return scoreUpper(all,6);
        case CHOICE: return scoreChoice(all); case FOUR_OF_A_KIND: return scoreFourKind(all);
        case FULL_HOUSE: return scoreFullHouse(all); case SMALL_STRAIGHT: return scoreSmallStraight(all);
        case LARGE_STRAIGHT: return scoreLargeStraight(all); case YACHT: return scoreYacht(all);
        default: return {0,pickSmallest(all,5)};
    }
}

struct Pick { Cat cat; int score; Cnt used; Cnt leftover; };
static Pick bestImmediatePick(const Cnt& all10, int remMask){
    Pick best{CHOICE,-1,Cnt{},Cnt{}};
    for(int ci=0; ci<CAT_CNT; ++ci){
        if(!(remMask&(1<<ci))) continue;
        auto pr=scoreByCat(all10,(Cat)ci);
        Cnt left=subCnt(all10,pr.second);
        if(pr.first>best.score){ best={ (Cat)ci, pr.first, pr.second, left}; }
    }
    if(best.score<0){ auto pr=scoreChoice(all10); Cnt left=subCnt(all10,pr.second); best={CHOICE,pr.first,pr.second,left}; }
    return best;
}

// ======== 5-dice state precompute for E_next ========
static vector<Cnt> states5; static vector<int> weight5;
static void gen5_rec(int face, int left, Cnt& cur){
    static const int fact[6]={1,1,2,6,24,120};
    if(face==6){ cur[6]=left; states5.push_back(cur);
        int n1=cur[1],n2=cur[2],n3=cur[3],n4=cur[4],n5=cur[5],n6=cur[6];
        int denom=fact[n1]*fact[n2]*fact[n3]*fact[n4]*fact[n5]*fact[n6];
        weight5.push_back(120/denom); return;
    }
    for(int k=0;k<=left;++k){ cur[face]=k; gen5_rec(face+1,left-k,cur); }
}
static void precompute_states5(){ states5.clear(); weight5.clear(); Cnt cur{}; gen5_rec(1,5,cur); }

static inline double E_next(const Cnt& L, int remMask){
    long long num=0;
    for(size_t i=0;i<states5.size();++i){
        Cnt all=addCnt(L, states5[i]);
        int sc=bestImmediateScore(all, remMask);
        num += (long long)sc * (long long)weight5[i];
    }
    return (double)num / 7776.0;
}

// ======== RNG ========
struct RNG {
    std::mt19937_64 eng;
    RNG(uint64_t s=0xC0FFEEULL){ std::seed_seq seq{(uint32_t)(s), (uint32_t)(s>>32)}; eng.seed(seq); }
    int uniform_int(int a,int b){ std::uniform_int_distribution<int> d(a,b); return d(eng); }
    double uniform(){ std::uniform_real_distribution<double> d(0.0,1.0); return d(eng); }
    double normal(double m=0.0,double s=1.0){ std::normal_distribution<double> d(m,s); return d(eng); }
};

// ======== Agent representation (trainable parameters) ========
// Focus on bidding; all caps/thresholds are also trainable.
struct AgentParams {
    // Linear policy for group choice and bid distribution
    // Features will be small hand-crafted vector φ
    int featDim=16;
    vector<float> w_group; // sigmoid(w_group·φ) -> P(A)
    vector<float> w_mu;    // bid mean (log space)
    vector<float> w_sigma; // bid std  (softplus)

    // Rule params (trainable, start from defaults)
    float ALPHA_SELF_BASE    = ALPHA_SELF_BASE_DEF;
    float DELTA_AVOID        = DELTA_AVOID_DEF;
    float SMALL_DELTA_ZERO   = SMALL_DELTA_ZERO_DEF;
    float COLLISION_CAP      = COLLISION_CAP_DEF;
    float NONCOLLISION_CAP   = NONCOLLISION_CAP_DEF;
    float ROI_MAX_RATIO      = ROI_MAX_RATIO_DEF;
    int   ZERO_BID_PERIOD    = ZERO_BID_PERIOD_DEF;
    int   ZERO_BID_PHASE     = ZERO_BID_PHASE_DEF;
    float BANKROLL_CAP       = BANKROLL_CAP_DEF;
    float BANKROLL_ALPHA_SCL = BANKROLL_ALPHA_SCL_DEF;
    float HEDGE_MARGIN_MIN   = HEDGE_MARGIN_MIN_DEF;
    float HEDGE_MARGIN_MAX   = HEDGE_MARGIN_MAX_DEF;

    void init(int d, RNG& rng){
        featDim = d;
        w_group.assign(d, 0.0f);
        w_mu.assign(d,    0.0f);
        w_sigma.assign(d,  -1.0f); // softplus(-1) ~ small std
        // small random
        for(int i=0;i<d;++i){
            w_group[i] += 0.02f * rng.normal();
            w_mu[i]    += 0.02f * rng.normal();
            w_sigma[i] += 0.02f * rng.normal();
        }
    }
};

struct Agent {
    AgentParams p;
    // online stats
    double rating=0.0;
};

// ======== Feature engineering for bidding ========
static void feats_bid(vector<double>& phi,
                      const Cnt& carry5, int remMask,
                      const vector<int>& A, const vector<int>& B,
                      int roundNo, int spentSoFar)
{
    phi.assign(0,0.0);
    // Build with fixed dim=16
    phi.resize(16, 0.0);

    Cnt cA = toCnt(A), cB = toCnt(B);
    double vA1 = E_next(cA, remMask);
    double vB1 = E_next(cB, remMask);

    // Immediate one-step with carry if available
    bool round1 = (diceCount(carry5)==0);
    auto V_self = [&](const Cnt& O)->double{
        if(round1) return E_next(O, remMask);
        Cnt all = addCnt(carry5, O);
        auto pick = bestImmediatePick(all, remMask);
        int rem2 = remMask & ~(1<<pick.cat);
        return (double)pick.score + E_next(pick.leftover, rem2);
    };
    double vA = V_self(cA);
    double vB = V_self(cB);

    double dSelf = fabs(vA - vB);
    double sA = sumDice(cA), sB = sumDice(cB);

    // Fill features
    phi[0]  = 1.0;
    phi[1]  = (double)roundNo / 13.0;
    phi[2]  = (double)spentSoFar / 100000.0;
    phi[3]  = (double)((remMask>>ONE)&1);
    phi[4]  = (double)((remMask>>SIX)&1);
    phi[5]  = vA / 60000.0; // scale
    phi[6]  = vB / 60000.0;
    phi[7]  = (vA - vB) / 30000.0;
    phi[8]  = dSelf / 30000.0;
    phi[9]  = sA / 30.0;
    phi[10] = sB / 30.0;
    // bitmask features for straights
    uint32_t mA = facesMask(cA), mB = facesMask(cB);
    phi[11] = (double)((mA&0x1F)==0x1F || (mA&0x3E)==0x3E);
    phi[12] = (double)((mB&0x1F)==0x1F || (mB&0x3E)==0x3E);
    // carry present
    phi[13] = round1 ? 0.0 : 1.0;
    // high die presence
    phi[14] = (cA[6]>=2);
    phi[15] = (cB[6]>=2);
}

// helpers
static double dot(const vector<float>& w, const vector<double>& x){
    double s=0; for(size_t i=0;i<w.size();++i) s += (double)w[i]*x[i]; return s;
}
static double sigmoid(double z){ return 1.0/(1.0+exp(-z)); }
static double softplus(double z){ return log1p(exp(z)); }

// ======== Bidding decision (policy-driven with rule caps) ========
struct BidDecision{ char group; int bid; double vA, vB, vA_opp, vB_opp; };

static BidDecision decideBid_policy(const AgentParams& P, RNG& rng,
    const Cnt& carry, int remMask,
    const vector<int>& A, const vector<int>& B,
    int oppRemMask, double oppAlphaEMA,
    int roundNo, int spentSoFar)
{
    bool round1 = (diceCount(carry)==0);
    Cnt cA=toCnt(A), cB=toCnt(B);

    auto V_self = [&](const Cnt& O){
        if(round1) return E_next(O, remMask);
        Cnt all=addCnt(carry, O);
        auto pick = bestImmediatePick(all, remMask);
        int rem2 = remMask & ~(1<<pick.cat);
        return (double)pick.score + E_next(pick.leftover, rem2);
    };
    double vA = V_self(cA), vB = V_self(cB);
    auto V_opp = [&](const Cnt& O){ return E_next(O, oppRemMask); };
    double vA_opp = V_opp(cA), vB_opp = V_opp(cB);

    vector<double> phi; feats_bid(phi, carry, remMask, A, B, roundNo, spentSoFar);

    // Group prob
    double pA = sigmoid(dot(P.w_group, phi));
    char gSelf = (rng.uniform() < pA ? 'A' : 'B');

    // Mean/Std for bid in log-space
    double mu    = dot(P.w_mu, phi);
    double sigma = softplus(dot(P.w_sigma, phi)); // >0
    double bidLog = mu + sigma * rng.normal();
    long long raw = llround(exp(bidLog));

    // ROI/alpha banking (mixed with learned bid)
    double dSelf = fabs(vA - vB);
    double alpha = P.ALPHA_SELF_BASE;
    if(spentSoFar >= (int)P.BANKROLL_CAP) alpha *= P.BANKROLL_ALPHA_SCL;
    raw = max<long long>(raw, (long long)floor(alpha * dSelf));

    // Opponent preferred group (heuristic)
    char gOpp  = (vA_opp>=vB_opp?'A':'B');
    double dOpp = fabs(vA_opp - vB_opp);

    // Zero-bid injection
    if(P.ZERO_BID_PERIOD>0 && (roundNo % P.ZERO_BID_PERIOD)==P.ZERO_BID_PHASE
       && gSelf==gOpp && dSelf<P.SMALL_DELTA_ZERO){
        return { gSelf, 0, vA, vB, vA_opp, vB_opp };
    }

    // Collision hedge
    if(gSelf==gOpp){
        double closeness = clampd(1.0 - fabs(dSelf - dOpp)/max(1.0, dSelf + dOpp), 0.0, 1.0);
        double margin = P.HEDGE_MARGIN_MIN + (P.HEDGE_MARGIN_MAX - P.HEDGE_MARGIN_MIN) * closeness;
        double need = oppAlphaEMA * dOpp + margin;
        if(need <= P.ROI_MAX_RATIO * dSelf) raw = max<long long>(raw, (long long)floor(need));
        raw = min<long long>(raw, (long long)P.COLLISION_CAP);
    }else{
        raw = min<long long>(raw, (long long)P.NONCOLLISION_CAP);
    }

    int bid = clampiLL(raw, 0, 100000);
    return { gSelf, bid, vA, vB, vA_opp, vB_opp };
}

// ======== Game simulation between two agents (self-play) ========
struct GameResult { int scoreA; int scoreB; int win; /*1,0,-1*/ int spentA; int spentB; };

static int randDie(RNG& rng){ return rng.uniform_int(1,6); }
static vector<int> roll5(RNG& rng){ vector<int> v(5); for(int i=0;i<5;++i) v[i]=randDie(rng); return v; }

static GameResult play_one(RNG& rng, const AgentParams& P1, const AgentParams& P2){
    // State per player
    Cnt carry1=zeroCnt(), carry2=zeroCnt();
    Cnt pending1=zeroCnt(), pending2=zeroCnt();
    int rem1 = (1<<CAT_CNT)-1, rem2 = (1<<CAT_CNT)-1;
    int oppRem1=rem2, oppRem2=rem1;
    double oppAlphaEMA1=1.0, oppAlphaEMA2=1.0;
    int spent1=0, spent2=0;
    int totalScore1=0, totalScore2=0;

    for(int roundNo=1; roundNo<=13; ++roundNo){
        // ROLL (skip bidding on 13th for next stage? Real rule: 13R no bidding; we simulate by just skipping bid phase)
        vector<int> A = roll5(rng), B = roll5(rng);

        if(roundNo!=13){
            auto d1 = decideBid_policy(P1, rng, carry1, rem1, A, B, oppRem1, oppAlphaEMA1, roundNo, spent1);
            auto d2 = decideBid_policy(P2, rng, carry2, rem2, A, B, oppRem2, oppAlphaEMA2, roundNo, spent2);

            // Assign groups
            char want1=d1.group, want2=d2.group;
            int bid1=d1.bid, bid2=d2.bid;

            // Resolve
            char got1, got2;
            if(want1!=want2){
                got1=want1; got2=want2;
            }else{
                if(bid1>bid2){ got1=want1; got2=(want1=='A'?'B':'A'); }
                else if(bid2>bid1){ got2=want2; got1=(want2=='A'?'B':'A'); }
                else { // coin flip
                    if(rng.uniform()<0.5){ got1=want1; got2=(want1=='A'?'B':'A'); }
                    else { got2=want2; got1=(want2=='A'?'B':'A'); }
                }
            }

            // Apply bidding scores (spend/earn)
            if(got1==want1) { totalScore1 -= bid1; spent1 += bid1; }
            else            { totalScore1 += bid1; }
            if(got2==want2) { totalScore2 -= bid2; spent2 += bid2; }
            else            { totalScore2 += bid2; }

            // Update carry/pending
            vector<int> gotA = (got1=='A')? A:B;
            vector<int> gotB2= (got2=='A')? A:B;
            Cnt gc1 = toCnt(gotA), gc2 = toCnt(gotB2);

            if(diceCount(carry1)==0){ carry1=gc1; pending1=zeroCnt(); } else { pending1=gc1; }
            if(diceCount(carry2)==0){ carry2=gc2; pending2=zeroCnt(); } else { pending2=gc2; }

            // Opponent EMA update (rough)
            double vA_opp = E_next(toCnt(A), oppRem1);
            double vB_opp = E_next(toCnt(B), oppRem1);
            double dOpp   = fabs(vA_opp - vB_opp);
            if(dOpp < 1.0) dOpp = 1.0;
            double ratio1  = clampd((double)bid2 / dOpp, 0.0, 2.0);
            const double DECAY = 0.85;
            oppAlphaEMA1 = clampd(DECAY * oppAlphaEMA1 + (1.0-DECAY)*ratio1, 0.5, 1.8);

            vA_opp = E_next(toCnt(A), oppRem2);
            vB_opp = E_next(toCnt(B), oppRem2);
            dOpp   = fabs(vA_opp - vB_opp);
            if(dOpp < 1.0) dOpp = 1.0;
            double ratio2  = clampd((double)bid1 / dOpp, 0.0, 2.0);
            oppAlphaEMA2 = clampd(DECAY * oppAlphaEMA2 + (1.0-DECAY)*ratio2, 0.5, 1.8);
        }

        // SCORE phase (skip in round 1)
        if(roundNo!=1){
            // P1
            {
                Cnt all = addCnt(carry1, pending1);
                auto pick = bestImmediatePick(all, rem1);
                totalScore1 += pick.score;
                carry1 = pick.leftover; pending1=zeroCnt(); rem1 &= ~(1<<pick.cat);
                oppRem2 = rem1;
            }
            // P2
            {
                Cnt all = addCnt(carry2, pending2);
                auto pick = bestImmediatePick(all, rem2);
                totalScore2 += pick.score;
                carry2 = pick.leftover; pending2=zeroCnt(); rem2 &= ~(1<<pick.cat);
                oppRem1 = rem2;
            }
        }
    }

    int win = (totalScore1>totalScore2)?1:((totalScore1<totalScore2)?-1:0);
    return { totalScore1, totalScore2, win, spent1, spent2 };
}

// ======== PBT (population-based training) ========
struct PopEntry { Agent agent; double fitness=0; int wins=0, losses=0, draws=0; };

static void mutate(AgentParams& P, RNG& rng, double scale){
    auto jitter = [&](float& v, double rel=0.05){
        double s = max(1e-6, fabs(v)*rel);
        v = (float)(v + rng.normal(0.0, s*scale));
    };
    for(auto& w: P.w_group) w += 0.05f * rng.normal(0.0, scale);
    for(auto& w: P.w_mu)    w += 0.05f * rng.normal(0.0, scale);
    for(auto& w: P.w_sigma) w += 0.05f * rng.normal(0.0, scale);

    jitter(P.ALPHA_SELF_BASE);
    jitter(P.DELTA_AVOID);
    jitter(P.SMALL_DELTA_ZERO);
    jitter(P.COLLISION_CAP);
    jitter(P.NONCOLLISION_CAP);
    jitter(P.ROI_MAX_RATIO, 0.02);
    // integer-like
    P.ZERO_BID_PERIOD = max(5, P.ZERO_BID_PERIOD + (int)lrint(rng.normal(0.0, 1.0*scale)));
    P.ZERO_BID_PHASE  = (P.ZERO_BID_PHASE + (int)lrint(rng.normal(0.0, 1.0*scale)) + P.ZERO_BID_PERIOD) % P.ZERO_BID_PERIOD;
    jitter(P.BANKROLL_CAP);
    jitter(P.BANKROLL_ALPHA_SCL, 0.02);
    jitter(P.HEDGE_MARGIN_MIN);
    jitter(P.HEDGE_MARGIN_MAX);
}

static void crossover(AgentParams& C, const AgentParams& A, const AgentParams& B, RNG& rng){
    C = A;
    for(size_t i=0;i<C.w_group.size();++i) if(rng.uniform()<0.5) C.w_group[i]=B.w_group[i];
    for(size_t i=0;i<C.w_mu.size();++i)    if(rng.uniform()<0.5) C.w_mu[i]=B.w_mu[i];
    for(size_t i=0;i<C.w_sigma.size();++i) if(rng.uniform()<0.5) C.w_sigma[i]=B.w_sigma[i];
    if(rng.uniform()<0.5) C.ALPHA_SELF_BASE=B.ALPHA_SELF_BASE;
    if(rng.uniform()<0.5) C.DELTA_AVOID=B.DELTA_AVOID;
    if(rng.uniform()<0.5) C.SMALL_DELTA_ZERO=B.SMALL_DELTA_ZERO;
    if(rng.uniform()<0.5) C.COLLISION_CAP=B.COLLISION_CAP;
    if(rng.uniform()<0.5) C.NONCOLLISION_CAP=B.NONCOLLISION_CAP;
    if(rng.uniform()<0.5) C.ROI_MAX_RATIO=B.ROI_MAX_RATIO;
    if(rng.uniform()<0.5) C.ZERO_BID_PERIOD=B.ZERO_BID_PERIOD;
    if(rng.uniform()<0.5) C.ZERO_BID_PHASE=B.ZERO_BID_PHASE;
    if(rng.uniform()<0.5) C.BANKROLL_CAP=B.BANKROLL_CAP;
    if(rng.uniform()<0.5) C.BANKROLL_ALPHA_SCL=B.BANKROLL_ALPHA_SCL;
    if(rng.uniform()<0.5) C.HEDGE_MARGIN_MIN=B.HEDGE_MARGIN_MIN;
    if(rng.uniform()<0.5) C.HEDGE_MARGIN_MAX=B.HEDGE_MARGIN_MAX;
}

// Opponent pool of frozen snapshots
struct Bank {
    int featDim=16;
    vector<AgentParams> pool;
};

static bool saveBank(const Bank& bank, const string& path="data.bin"){
    ofstream f(path, ios::binary); if(!f) return false;
    uint64_t magic = 0x5941434854415543ull; // "YACHTAUC"
    uint32_t ver=1, cnt=bank.pool.size(), dim=bank.featDim;
    f.write((char*)&magic,8); f.write((char*)&ver,4); f.write((char*)&cnt,4); f.write((char*)&dim,4);
    for(auto& P: bank.pool){
        auto write_vec = [&](const vector<float>& v){ uint32_t n=v.size(); f.write((char*)&n,4); f.write((char*)v.data(), n*sizeof(float)); };
        write_vec(P.w_group); write_vec(P.w_mu); write_vec(P.w_sigma);
        f.write((char*)&P.ALPHA_SELF_BASE, sizeof(float));
        f.write((char*)&P.DELTA_AVOID, sizeof(float));
        f.write((char*)&P.SMALL_DELTA_ZERO, sizeof(float));
        f.write((char*)&P.COLLISION_CAP, sizeof(float));
        f.write((char*)&P.NONCOLLISION_CAP, sizeof(float));
        f.write((char*)&P.ROI_MAX_RATIO, sizeof(float));
        f.write((char*)&P.ZERO_BID_PERIOD, sizeof(int));
        f.write((char*)&P.ZERO_BID_PHASE, sizeof(int));
        f.write((char*)&P.BANKROLL_CAP, sizeof(float));
        f.write((char*)&P.BANKROLL_ALPHA_SCL, sizeof(float));
        f.write((char*)&P.HEDGE_MARGIN_MIN, sizeof(float));
        f.write((char*)&P.HEDGE_MARGIN_MAX, sizeof(float));
    }
    return true;
}

// ======== Training loop ========
int main(){
    ios::sync_with_stdio(false);
    precompute_states5();

    RNG rng(12345);

    const int FEAT_DIM = 16;
    const int POP_N = 32;           // population size
    const int GENS  = 200;          // generations
    const int MATCHES_PER = 40;     // matches per agent per gen (vs random peers + pool)
    const int POOL_KEEP = 8;        // # of frozen agents to export
    const double MUT_START = 1.0, MUT_END = 0.2;

    // init population
    vector<PopEntry> pop(POP_N);
    for(int i=0;i<POP_N;++i){
        pop[i].agent.p.init(FEAT_DIM, rng);
    }
    Bank bank; bank.featDim = FEAT_DIM;
    // seed pool with one random
    bank.pool.push_back(pop[0].agent.p);

    for(int gen=0; gen<GENS; ++gen){
        // evaluate
        for(auto& e: pop){ e.fitness=0; e.wins=e.losses=e.draws=0; }

        for(int i=0;i<POP_N;++i){
            for(int m=0;m<MATCHES_PER;++m){
                // pick opponent: 50% from population, 50% from bank
                bool fromPool = (rng.uniform()<0.5 && !bank.pool.empty());
                int j;
                if(fromPool){
                    j = -1; // indicate pool
                }else{
                    do{ j=rng.uniform_int(0, POP_N-1); }while(j==i);
                }
                AgentParams opp = fromPool ? bank.pool[rng.uniform_int(0, (int)bank.pool.size()-1)]
                                            : pop[j].agent.p;

                // two games with swap to reduce first-mover/random variance
                auto g1 = play_one(rng, pop[i].agent.p, opp);
                auto g2 = play_one(rng, opp, pop[i].agent.p);
                int my1 = g1.scoreA - g1.scoreB;
                int my2 = g2.scoreB - g2.scoreA; // swapped
                int winCount = (my1>0) + (my2>0);
                int drawCount= (my1==0) + (my2==0);
                double fitness = 0.5 * ( (double)my1 + (double)my2 ); // score margin average

                pop[i].fitness += fitness;
                pop[i].wins += winCount;
                pop[i].draws += drawCount;
                pop[i].losses += 2 - winCount - drawCount;
            }
        }

        // rank
        vector<int> idx(POP_N); iota(idx.begin(), idx.end(), 0);
        sort(idx.begin(), idx.end(), [&](int a,int b){
            if(pop[a].wins != pop[b].wins) return pop[a].wins > pop[b].wins;
            if(pop[a].fitness != pop[b].fitness) return pop[a].fitness > pop[b].fitness;
            return pop[a].draws > pop[b].draws;
        });

        // print brief log
        auto& top = pop[idx[0]];
        cerr << "Gen " << gen
             << " | top wins="<<top.wins<<" draws="<<top.draws<<" losses="<<top.losses
             << " fitness="<<fixed<<setprecision(1)<<top.fitness << "\n";

        // snapshot champion to pool (diversify)
        if(bank.pool.empty() || gen%3==0){
            bank.pool.push_back(top.agent.p);
            if((int)bank.pool.size()>32) bank.pool.erase(bank.pool.begin());
        }

        // evolve: keep top 25%, refill rest by crossover+mutation
        int keep = max(1, POP_N/4);
        vector<AgentParams> nextParams; nextParams.reserve(POP_N);
        for(int k=0;k<keep;++k) nextParams.push_back(pop[idx[k]].agent.p);

        double mutScale = MUT_START + (MUT_END-MUT_START)*(double)gen/(double)GENS;
        while((int)nextParams.size()<POP_N){
            int a = rng.uniform_int(0, keep-1);
            int b = rng.uniform_int(0, keep-1);
            AgentParams child; crossover(child, pop[idx[a]].agent.p, pop[idx[b]].agent.p, rng);
            mutate(child, rng, mutScale);
            nextParams.push_back(child);
        }
        for(int i=0;i<POP_N;++i) pop[i].agent.p = nextParams[i];

        // Occasionally prune pool to best few against current champ
        if(gen%10==0){
            // evaluate pool vs champ quickly
            AgentParams champ = pop[idx[0]].agent.p;
            vector<pair<double,int>> scores; scores.reserve(bank.pool.size());
            for(int i=0;i<(int)bank.pool.size();++i){
                auto g1 = play_one(rng, champ, bank.pool[i]);
                auto g2 = play_one(rng, bank.pool[i], champ);
                int s = (g1.scoreA-g1.scoreB) - (g2.scoreA-g2.scoreB);
                scores.push_back({(double)s, i});
            }
            sort(scores.begin(), scores.end(), greater<>());
            // keep top POOL_KEEP
            vector<AgentParams> newPool;
            for(int i=0;i<(int)scores.size() && (int)newPool.size()<POOL_KEEP; ++i){
                newPool.push_back(bank.pool[scores[i].second]);
            }
            bank.pool = newPool;
        }
    }

    // Export: champion + a few alternates
    // Rebuild minimal pool: champion + up to POOL_KEEP-1 others
    // Here we keep whatever bank currently has; ensure size<=POOL_KEEP
    while((int)bank.pool.size()>POOL_KEEP) bank.pool.pop_back();
    if(bank.pool.empty()) bank.pool.push_back(pop[0].agent.p);

    bool ok = saveBank(bank, "data.bin");
    cerr << (ok? "Saved data.bin (" : "Failed saving data.bin (")
         << bank.pool.size() << " agents)\n";
    return 0;
}
