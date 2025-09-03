// player.cpp
// Yacht Auction — tournament player that loads data.bin (bank of agents) and plays.
// Build: g++ -O3 -std=c++17 -o player player.cpp
// Run:   ./player  (interacts via stdin/stdout per problem protocol)

#include <bits/stdc++.h>
using namespace std;

// ===================== Shared game utilities (same spirit as sample) =====================
enum Cat { ONE, TWO, THREE, FOUR, FIVE, SIX,
           CHOICE, FOUR_OF_A_KIND, FULL_HOUSE, SMALL_STRAIGHT, LARGE_STRAIGHT, YACHT,
           CAT_CNT };
static const char* CatName[CAT_CNT] = {
    "ONE","TWO","THREE","FOUR","FIVE","SIX",
    "CHOICE","FOUR_OF_A_KIND","FULL_HOUSE","SMALL_STRAIGHT","LARGE_STRAIGHT","YACHT"
};

using Cnt = array<int,7>; // 1..6

inline Cnt zeroCnt(){ Cnt c{}; return c; }
inline int diceCount(const Cnt& c){ int s=0; for(int f=1;f<=6;++f) s+=c[f]; return s; }
inline Cnt toCnt(const vector<int>& v){ Cnt c{}; for(int x: v) ++c[x]; return c; }
inline Cnt addCnt(Cnt a, const Cnt& b){ for(int f=1;f<=6;++f) a[f]+=b[f]; return a; }
inline Cnt subCnt(Cnt a, const Cnt& b){ for(int f=1;f<=6;++f) a[f]-=b[f]; return a; }
inline vector<int> expandCnt(const Cnt& c){ vector<int> v; v.reserve(5); for(int f=1;f<=6;++f) for(int k=0;k<c[f];++k) v.push_back(f); return v; }
inline int sumDice(const Cnt& c){ int s=0; for(int f=1;f<=6;++f) s+=f*c[f]; return s; }
inline double clampd(double x, double a, double b){ return x<a?a:(x>b?b:x); }
inline int clampiLL(long long x, int lo, int hi){ if(x<lo) return lo; if(x>hi) return hi; return (int)x; }
inline uint32_t facesMask(const Cnt& c){ uint32_t m=0; for(int f=1;f<=6;++f) if(c[f]>0) m|=(1u<<(f-1)); return m; }
static Cnt pickSmallest(const Cnt& c, int need){ Cnt t{}; int left=need; for(int f=1;f<=6&&left>0;++f){int k=min(c[f],left); t[f]=k; left-=k;} return t; }
static Cnt pickLargest(const Cnt& c, int need){ Cnt t{}; int left=need; for(int f=6;f>=1&&left>0;--f){int k=min(c[f],left); t[f]=k; left-=k;} return t; }

// ---------- Immediate scoring ----------
static inline int scoreUpperOnly(const Cnt& all, int face){ int use=min(all[face],5); return use*face*1000; }
static inline int scoreChoiceOnly(const Cnt& all){ int need=5, s=0; for(int f=6; f>=1 && need>0; --f){ int t=min(all[f],need); s+=t*f; need-=t; } return s*1000; }
static inline int scoreFourKindOnly(const Cnt& all){
    int best=0; for(int f=1;f<=6;++f) if(all[f]>=4){
        int s=4*f; for(int g=6; g>=1; --g){ if(g==f) continue; if(all[g]>0){ s+=g; break; } }
        best=max(best, s*1000);
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

// Build used dice for each category
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

// ---------- 5-dice state precompute for E_next ----------
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

// ===================== Model (data.bin) structures =====================
struct AgentParams {
    int featDim=16;
    vector<float> w_group, w_mu, w_sigma;

    float ALPHA_SELF_BASE    = 0.95f;
    float DELTA_AVOID        = 1500.f;
    float SMALL_DELTA_ZERO   = 1200.f;
    float COLLISION_CAP      = 6000.f;
    float NONCOLLISION_CAP   = 12000.f;
    float ROI_MAX_RATIO      = 1.00f;
    int   ZERO_BID_PERIOD    = 23;
    int   ZERO_BID_PHASE     = 7;
    float BANKROLL_CAP       = 75000.f;
    float BANKROLL_ALPHA_SCL = 0.80f;
    float HEDGE_MARGIN_MIN   = 400.f;
    float HEDGE_MARGIN_MAX   = 900.f;
};

struct Bank {
    int featDim=16;
    vector<AgentParams> pool;
};

static bool loadBank(Bank& bank, const string& path="data.bin"){
    ifstream f(path, ios::binary); if(!f) return false;
    uint64_t magic; uint32_t ver, cnt, dim;
    f.read((char*)&magic,8); f.read((char*)&ver,4); f.read((char*)&cnt,4); f.read((char*)&dim,4);
    if(!f || magic!=0x5941434854415543ull) return false; // "YACHTAUC"
    bank.featDim = (int)dim;
    bank.pool.resize(cnt);
    auto read_vec = [&](vector<float>& v){
        uint32_t n=0; f.read((char*)&n,4); v.resize(n);
        if(n) f.read((char*)v.data(), n*sizeof(float));
    };
    for(uint32_t i=0;i<cnt;++i){
        AgentParams P;
        read_vec(P.w_group); read_vec(P.w_mu); read_vec(P.w_sigma);
        f.read((char*)&P.ALPHA_SELF_BASE, sizeof(float));
        f.read((char*)&P.DELTA_AVOID, sizeof(float));
        f.read((char*)&P.SMALL_DELTA_ZERO, sizeof(float));
        f.read((char*)&P.COLLISION_CAP, sizeof(float));
        f.read((char*)&P.NONCOLLISION_CAP, sizeof(float));
        f.read((char*)&P.ROI_MAX_RATIO, sizeof(float));
        f.read((char*)&P.ZERO_BID_PERIOD, sizeof(int));
        f.read((char*)&P.ZERO_BID_PHASE, sizeof(int));
        f.read((char*)&P.BANKROLL_CAP, sizeof(float));
        f.read((char*)&P.BANKROLL_ALPHA_SCL, sizeof(float));
        f.read((char*)&P.HEDGE_MARGIN_MIN, sizeof(float));
        f.read((char*)&P.HEDGE_MARGIN_MAX, sizeof(float));
        P.featDim = bank.featDim;
        bank.pool[i] = std::move(P);
    }
    return true;
}

// ===================== Inference: policy-driven bidding =====================
struct RNG {
    std::mt19937_64 eng;
    RNG(){ std::random_device rd; uint64_t s = ((uint64_t)rd()<<32) ^ (uint64_t)chrono::high_resolution_clock::now().time_since_epoch().count(); eng.seed(s); }
    double uniform(){ std::uniform_real_distribution<double> d(0.0,1.0); return d(eng); }
    double normal(double m=0.0,double s=1.0){ std::normal_distribution<double> d(m,s); return d(eng); }
};

static double dot(const vector<float>& w, const vector<double>& x){
    double s=0; size_t n=min(w.size(), x.size()); for(size_t i=0;i<n;++i) s += (double)w[i]*x[i]; return s;
}
static double sigmoid(double z){ return 1.0/(1.0+exp(-z)); }
static double softplus(double z){ return log1p(exp(z)); }

static void feats_bid(vector<double>& phi,
                      const Cnt& carry5, int remMask,
                      const vector<int>& A, const vector<int>& B,
                      int roundNo, int spentSoFar)
{
    phi.assign(16, 0.0);
    Cnt cA = toCnt(A), cB = toCnt(B);
    double vA1 = E_next(cA, remMask);
    double vB1 = E_next(cB, remMask);

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
    uint32_t mA = facesMask(cA), mB = facesMask(cB);

    phi[0]  = 1.0;
    phi[1]  = (double)roundNo / 13.0;
    phi[2]  = (double)spentSoFar / 100000.0;
    phi[3]  = (double)((remMask>>ONE)&1);
    phi[4]  = (double)((remMask>>SIX)&1);
    phi[5]  = vA / 60000.0;
    phi[6]  = vB / 60000.0;
    phi[7]  = (vA - vB) / 30000.0;
    phi[8]  = dSelf / 30000.0;
    phi[9]  = sA / 30.0;
    phi[10] = sB / 30.0;
    phi[11] = (double)((mA&0x1F)==0x1F || (mA&0x3E)==0x3E);
    phi[12] = (double)((mB&0x1F)==0x1F || (mB&0x3E)==0x3E);
    phi[13] = round1 ? 0.0 : 1.0;
    phi[14] = (cA[6]>=2);
    phi[15] = (cB[6]>=2);
}

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
    double pA = P.w_group.empty()? (vA>=vB?1.0:0.0) : sigmoid(dot(P.w_group, phi));
    char gSelf = ( (P.w_group.empty() ? (vA>=vB) : (rng.uniform() < pA)) ? 'A' : 'B');

    // Mean/Std for bid in log-space
    double mu    = P.w_mu.empty()? log(max(1.0, fabs(vA-vB))) : dot(P.w_mu, phi);
    double sigma = P.w_sigma.empty()? 0.3 : softplus(dot(P.w_sigma, phi)); // >0
    double bidLog = mu + sigma * rng.normal();
    long long raw = llround(exp(bidLog));

    // ROI/alpha banking
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

// ===================== Protocol player main =====================
static int catFromString(const string& s){
    if(s=="ONE")return ONE; if(s=="TWO")return TWO; if(s=="THREE")return THREE; if(s=="FOUR")return FOUR;
    if(s=="FIVE")return FIVE; if(s=="SIX")return SIX; if(s=="CHOICE")return CHOICE; if(s=="FOUR_OF_A_KIND")return FOUR_OF_A_KIND;
    if(s=="FULL_HOUSE")return FULL_HOUSE; if(s=="SMALL_STRAIGHT")return SMALL_STRAIGHT; if(s=="LARGE_STRAIGHT")return LARGE_STRAIGHT;
    if(s=="YACHT")return YACHT; return -1;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute_states5();
    RNG rng;

    // Load bank (data.bin). If absent, run with fallback (empty pool -> default heuristic)
    Bank bank;
    bool hasBank = loadBank(bank, "data.bin");
    if(!hasBank){
        // fallback: one default agent with empty weights (heuristic path will kick in)
        assert(false);
    }

    // pick which agent to use: champion(0) or random
    AgentParams P = bank.pool[0];
    // (원하면 랜덤으로: P = bank.pool[rng.eng()%bank.pool.size()];)

    // Game runtime states
    Cnt carry = zeroCnt();     // after scoring we keep leftover (5 dice except R1)
    Cnt pending = zeroCnt();
    int remMask = (1<<CAT_CNT) - 1;

    int oppRemMask = (1<<CAT_CNT) - 1;
    double oppAlphaEMA = 1.0;

    vector<int> lastA(5), lastB(5);
    int roundNo = 0;

    int spentSoFar = 0;
    char lastChosenGroup = 'A';
    int  lastBidValue = 0;

    string cmd;
    while(cin >> cmd){
        if(cmd=="READY"){
            cout << "OK\n" << flush;
        }
        else if(cmd=="ROUND"){
            cin >> roundNo; // optional, if judge sends
        }
        else if(cmd=="ROLL"){
            string sA, sB; cin >> sA >> sB;
            for(int i=0;i<5;++i){ lastA[i]=sA[i]-'0'; lastB[i]=sB[i]-'0'; }

            auto d = decideBid_policy(P, rng, carry, remMask, lastA, lastB, oppRemMask, oppAlphaEMA, roundNo, spentSoFar);
            lastChosenGroup = d.group;
            lastBidValue    = d.bid;
            cout << "BID " << d.group << ' ' << d.bid << "\n" << flush;
        }
        else if(cmd=="GET"){
            char g, g0; int x0; cin >> g >> g0 >> x0;

            // got dice
            vector<int> got = (g=='A')? lastA : lastB;
            Cnt gc = toCnt(got);
            if(diceCount(carry)==0){ carry = gc; pending = zeroCnt(); }
            else { pending = gc; }

            // update spending if we got what we wanted
            if(g == lastChosenGroup){
                spentSoFar += lastBidValue;
            }

            // update opponent alpha EMA (rough estimator)
            Cnt cA=toCnt(lastA), cB=toCnt(lastB);
            double vA_opp = E_next(cA, oppRemMask);
            double vB_opp = E_next(cB, oppRemMask);
            double dOpp   = fabs(vA_opp - vB_opp);
            if(dOpp < 1.0) dOpp = 1.0;
            double ratio  = clampd((double)x0 / dOpp, 0.0, 2.0);
            const double DECAY = 0.85;
            oppAlphaEMA = clampd(DECAY * oppAlphaEMA + (1.0-DECAY)*ratio, 0.5, 1.8);
        }
        else if(cmd=="SCORE"){
            // round 1: skip scoring per rules, but judge still may call SCORE then expect PUT quickly for later rounds
            Cnt all = addCnt(carry, pending);
            auto pick = bestImmediatePick(all, remMask);
            vector<int> used = expandCnt(pick.used);
            if((int)used.size()<5){
                Cnt rest=subCnt(all, pick.used);
                Cnt pad=pickSmallest(rest,5-(int)used.size());
                Cnt fixed=addCnt(pick.used,pad);
                used=expandCnt(fixed);
                pick.leftover=subCnt(all,fixed);
            }
            string token; token.reserve(5); for(int i=0;i<5;++i) token.push_back(char('0'+used[i]));
            cout << "PUT " << CatName[pick.cat] << ' ' << token << "\n" << flush;
            carry = pick.leftover; pending = zeroCnt(); remMask &= ~(1<<pick.cat);
        }
        else if(cmd=="SET"){
            string cname, d; cin >> cname >> d;
            int ci = catFromString(cname);
            if(ci>=0) oppRemMask &= ~(1<<ci);
            // (상대 dice d는 별도 사용 안 함)
        }
        else if(cmd=="FINISH"){
            break;
        }
        // 기타 알 수 없는 커맨드는 무시
    }
    return 0;
}
