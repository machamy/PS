#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <iostream>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

// ===== Rules =====
enum DiceRule {
    ONE, TWO, THREE, FOUR, FIVE, SIX,
    CHOICE, FOUR_OF_A_KIND, FULL_HOUSE, SMALL_STRAIGHT, LARGE_STRAIGHT, YACHT
};

struct Bid { char group; int amount; };
struct DicePut { DiceRule rule; vector<int> dice; };

struct GameState {
    vector<int> dice;            // 5 or 10
    int ruleScore[12];           // -1 if unused
    int bidScore;                // +/-

    GameState() : bidScore(0) { fill(begin(ruleScore), end(ruleScore), -1); }

    inline int getTotalScore() const {
        int basic=0, comb=0;
        for(int i=0;i<6;i++) if(ruleScore[i]!=-1) basic += ruleScore[i];
        for(int i=6;i<12;i++) if(ruleScore[i]!=-1) comb  += ruleScore[i];
        int bonus = (basic>=63000)?35000:0;
        return basic + bonus + comb + bidScore;
    }
    inline void bid(bool ok, int amt){ bidScore += ok ? -amt : +amt; }
    inline void addDice(const vector<int>& v){ dice.insert(dice.end(), v.begin(), v.end()); }
    void useDice(const DicePut& put) {
        assert(ruleScore[put.rule]==-1);
        // consume exactly 5 dice (value-match 삭제)
        for(int d: put.dice){
            auto it = find(dice.begin(), dice.end(), d);
            assert(it!=dice.end());
            dice.erase(it);
        }
        ruleScore[put.rule] = calculateScore(put);
    }
    static int calculateScore(const DicePut& put); // non-hot fallback
};

// ===== Heuristic Params =====
static const int kMaxScore[12] = {
    5000,10000,15000,20000,25000,30000, // ONE..SIX
    30000,30000,30000,15000,30000,50000 // CHOICE..YACHT
};
static const int kWastePenalty[12] = {
    0,0,0,0,0,0, 0, 10000,8000,6000,12000,20000
};
static const int kQualityBonus[12] = {
    500,600,800,1000,1200,1500, 300,1200,900,700,1200,2000
};
static const int UPPER_MAX_SUM_PER_RULE[6] = {5000,10000,15000,20000,25000,30000};

// ===== Precomputed tables (loaded from data.bin or built once) =====
// 테이블 크기: 46,656 상태 × (valid 1B + 12 score × 4B) ≈ 2.3MB
static uint8_t* PRE_VALID = nullptr;      // [46656]
static int32_t* PRE_BASE  = nullptr;      // [46656 * 12]

// C(10,5)=252 조합 인덱스
static array<array<uint8_t,5>,252> COMB10;
static bool COMB10_READY = false;

// ===== IO-safe header =====
struct BinHeader {
    char magic[8];     // "YACHTAI"
    uint32_t version;  // 1
    uint32_t validN;   // 46656
    uint32_t rulesN;   // 12
};

// ===== Safe alloc/free =====
static void alloc_tables() {
    if (!PRE_VALID) PRE_VALID = (uint8_t*)malloc(46656);
    if (!PRE_BASE)  PRE_BASE  = (int32_t*)malloc(46656 * 12 * sizeof(int32_t));
    if (!PRE_VALID || !PRE_BASE) {
        fprintf(stderr, "Allocation failed\n");
        exit(1);
    }
}
static void free_tables() {
    if (PRE_VALID) { free(PRE_VALID); PRE_VALID=nullptr; }
    if (PRE_BASE)  { free(PRE_BASE);  PRE_BASE=nullptr; }
}

// ===== Build COMB10 once (quick) =====
static void build_comb10() {
    if (COMB10_READY) return;
    int idx=0;
    for (int a=0;a<6;a++)
    for (int b=a+1;b<7;b++)
    for (int d=b+1;d<8;d++)
    for (int e=d+1;e<9;e++)
    for (int f=e+1;f<10;f++) {
        COMB10[idx++] = { (uint8_t)a,(uint8_t)b,(uint8_t)d,(uint8_t)e,(uint8_t)f };
    }
    COMB10_READY = true;
}

// ===== Encode counts to id =====
static inline int encodeCounts(const int c[7]){
    // base-6 encoding c1..c6 (each in [0..5])
    int id=0;
    for(int i=1;i<=6;i++){ id = id*6 + c[i]; }
    return id;
}

// ===== Precompute quickly (≈ 46k states) =====
static void precompute_all_fast() {
    alloc_tables();
    for(int c1=0;c1<=5;c1++)
    for(int c2=0;c2<=5;c2++)
    for(int c3=0;c3<=5;c3++)
    for(int c4=0;c4<=5;c4++)
    for(int c5=0;c5<=5;c5++)
    for(int c6=0;c6<=5;c6++){
        const int sumc = c1+c2+c3+c4+c5+c6;
        const int id = (((((c1)*6+c2)*6+c3)*6+c4)*6+c5)*6+c6;
        if (sumc!=5) { PRE_VALID[id]=0; continue; }
        PRE_VALID[id]=1;

        int cnt[7]={0,c1,c2,c3,c4,c5,c6};
        const int sum = c1*1 + c2*2 + c3*3 + c4*4 + c5*5 + c6*6;

        // basic
        PRE_BASE[id*12 + ONE]   = c1*1000;
        PRE_BASE[id*12 + TWO]   = c2*2000;
        PRE_BASE[id*12 + THREE] = c3*3000;
        PRE_BASE[id*12 + FOUR]  = c4*4000;
        PRE_BASE[id*12 + FIVE]  = c5*5000;
        PRE_BASE[id*12 + SIX]   = c6*6000;
        PRE_BASE[id*12 + CHOICE]= sum*1000;

        bool four=false, yacht=false, has2=false, has3=false;
        for(int i=1;i<=6;i++){
            if(cnt[i]>=4) four=true;
            if(cnt[i]==5) yacht=true;
            if(cnt[i]==2 || cnt[i]==5) has2=true;
            if(cnt[i]==3 || cnt[i]==5) has3=true;
        }
        PRE_BASE[id*12 + FOUR_OF_A_KIND] = four ? sum*1000 : 0;
        PRE_BASE[id*12 + FULL_HOUSE]     = (has2 && has3) ? sum*1000 : 0;

        int mask = 0;
        for(int i=1;i<=6;i++) if(cnt[i]) mask |= (1<<(i-1));
        const bool sm = ((mask & 0b1111)==0b1111) || (((mask>>1)&0b1111)==0b1111) || (((mask>>2)&0b1111)==0b1111);
        PRE_BASE[id*12 + SMALL_STRAIGHT] = sm ? 15000 : 0;
        PRE_BASE[id*12 + LARGE_STRAIGHT] = (mask==31 || mask==62) ? 30000 : 0;
        PRE_BASE[id*12 + YACHT]          = yacht ? 50000 : 0;
    }
}

// ===== Save / Load data.bin =====
static bool load_data_bin(const char* path="data.bin") {
    alloc_tables();
    ifstream fin(path, ios::binary);
    if (!fin.good()) return false;
    BinHeader h{};
    fin.read((char*)&h, sizeof(h));
    if (!fin.good()) return false;
    if (memcmp(h.magic,"YACHTAI",7)!=0 || h.version!=1 || h.validN!=46656 || h.rulesN!=12) return false;
    fin.read((char*)PRE_VALID, 46656);
    fin.read((char*)PRE_BASE,  46656*12*sizeof(int32_t));
    return fin.good();
}
static bool save_data_bin(const char* path="data.bin") {
    ofstream fout(path, ios::binary|ios::trunc);
    if (!fout.good()) return false;
    BinHeader h{};
    memcpy(h.magic,"YACHTAI",7);
    h.version=1; h.validN=46656; h.rulesN=12;
    fout.write((const char*)&h, sizeof(h));
    fout.write((const char*)PRE_VALID, 46656);
    fout.write((const char*)PRE_BASE,  46656*12*sizeof(int32_t));
    return fout.good();
}

// ===== Quick helpers =====
static inline vector<DiceRule> availableRules(const GameState& st) {
    vector<DiceRule> v; v.reserve(12);
    for(int r=0;r<12;r++) if (st.ruleScore[r]==-1) v.push_back((DiceRule)r);
    return v;
}
static inline int upperSumNow(const GameState& st) {
    int s=0; for(int i=0;i<6;i++) if (st.ruleScore[i]!=-1) s+=st.ruleScore[i]; return s;
}
static inline int upperRemainMaxSum(const GameState& st) {
    int s=0;
    for(int i=0;i<6;i++) if (st.ruleScore[i]==-1) s+=UPPER_MAX_SUM_PER_RULE[i];
    return s;
}

// ===== Core evaluator using precomputed tables =====
static pair<int, DicePut> bestPutForPool(const vector<int>& pool, const GameState& state) {
    const int n = (int)pool.size();
    auto rules = availableRules(state);
    const int S0 = upperSumNow(state);
    const int remainSum = upperRemainMaxSum(state);
    const bool beforeReachable = (S0 + remainSum >= 63000);

    int bestVal = -1000000000;
    DiceRule bestRule = CHOICE;
    array<uint8_t,5> bestIdx = {0,1,2,3,4};

    auto evalFiveByIdx = [&](int i0,int i1,int i2,int i3,int i4){
        int c[7]={0};
        const int v0=pool[i0], v1=pool[i1], v2=pool[i2], v3=pool[i3], v4=pool[i4];
        c[v0]++; c[v1]++; c[v2]++; c[v3]++; c[v4]++;
        const int id = encodeCounts(c);
        if (!PRE_VALID[id]) return;

        const int32_t* base = &PRE_BASE[id*12];
        for (DiceRule r : rules) {
            int b = base[r];
            int qBonus = (kMaxScore[r] ? (b * kQualityBonus[r]) / kMaxScore[r] : 0);
            int waste  = (b==0 ? kWastePenalty[r] : 0);

            int s1 = S0 + ((r<=SIX) ? b : 0);
            // "이번에 사용한 upper rule"을 남은 최대 합에서 제외 (대략치)
            int remainMinus = remainSum - ((r<=SIX && state.ruleScore[r]==-1) ? UPPER_MAX_SUM_PER_RULE[r] : 0);
            int bonusDelta = (s1 >= 63000 && S0 < 63000) ? 35000 : 0;
            bool afterReachable = (s1 + remainMinus >= 63000);
            int killPenalty = (!afterReachable && beforeReachable ? 12000 : 0);

            int utility = b + qBonus - waste + bonusDelta - killPenalty;
            if ((r==YACHT || r==LARGE_STRAIGHT) && b==0) utility -= 4000;

            if (utility > bestVal) {
                bestVal = utility;
                bestRule = r;
                bestIdx = {(uint8_t)i0,(uint8_t)i1,(uint8_t)i2,(uint8_t)i3,(uint8_t)i4};
            }
        }
    };

    if (n==5) {
        evalFiveByIdx(0,1,2,3,4);
    } else if (n==10) {
        if (!COMB10_READY) build_comb10();
        for (const auto& idx : COMB10) {
            evalFiveByIdx(idx[0],idx[1],idx[2],idx[3],idx[4]);
        }
    } else { // 6..9 (특수상황 거의 없음)
        vector<int> bit(n,0); fill(bit.begin(), bit.begin()+5, 1);
        do {
            int p[5], k=0;
            for (int i=0;i<n;i++) if (bit[i]) p[k++]=i;
            evalFiveByIdx(p[0],p[1],p[2],p[3],p[4]);
        } while (prev_permutation(bit.begin(), bit.end()));
    }

    vector<int> bestDice(5);
    for (int i=0;i<5;i++) bestDice[i] = pool[bestIdx[i]];
    return {bestVal, DicePut{bestRule, move(bestDice)}};
}

static inline int myValueWith(const vector<int>& bundle, const GameState& me) {
    GameState pseudo = me;
    vector<int> pool = pseudo.dice;
    pool.insert(pool.end(), bundle.begin(), bundle.end());
    return bestPutForPool(pool, pseudo).first;
}
static inline int oppValueBundleOnly(const vector<int>& bundle, const GameState& opp) {
    GameState pseudo = opp;
    return bestPutForPool(bundle, pseudo).first;
}

static inline long long llround(double x) {
    return (x >= 0.0) ? static_cast<long long>(x + 0.5) : static_cast<long long>(x - 0.5);
}

// ===== AI Game =====
class Game {
public:
    GameState myState;
    GameState oppState;

    Bid     calculateBid(const vector<int>& diceA, const vector<int>& diceB) {
        int myA = myValueWith(diceA, myState);
        int myB = myValueWith(diceB, myState);
        int opA = oppValueBundleOnly(diceA, oppState);
        int opB = oppValueBundleOnly(diceB, oppState);

        char myPref  = (myA > myB ? 'A' : (myB > myA ? 'B' : 'A'));
        char oppPref = (opA > opB ? 'A' : (opB > opA ? 'B' : 'A'));

        if (myPref != oppPref) return Bid{myPref, 0};

        int myPrefVal = (myPref=='A' ? myA : myB);
        int myAltVal  = (myPref=='A' ? myB : myA);
        int oppPrefVal= (oppPref=='A' ? opA : opB);
        int oppAltVal = (oppPref=='A' ? opB : opA);

        int myMarg  = max(0, myPrefVal - myAltVal);
        int oppMarg = max(0, oppPrefVal - oppAltVal);

        int xStar = myMarg / 2;
        int yStar = oppMarg / 2;

        int diff = myState.getTotalScore() - oppState.getTotalScore();
        double aggr = 1.0;
        if (diff <= -30000) aggr = 1.25;
        else if (diff >=  30000) aggr = 0.85;

        long long bidLL = llround(aggr * (max(xStar, yStar + 1)));
        if (bidLL < 0) bidLL = 0;
        if (bidLL > 100000) bidLL = 100000;
        bidLL = min<long long>(bidLL, myMarg);
        return Bid{myPref, (int)bidLL};
    }

    DicePut calculatePut() {
        auto best = bestPutForPool(myState.dice, myState);
        return best.second;
    }

    void updateGet(vector<int> diceA, vector<int> diceB, Bid myBid, Bid oppBid, char myGroup) {
        if (myGroup == 'A') { myState.addDice(diceA); oppState.addDice(diceB); }
        else                { myState.addDice(diceB); oppState.addDice(diceA); }
        bool myBidOk  = (myBid.group == myGroup);
        myState.bid(myBidOk, myBid.amount);
        char oppGroup = (myGroup == 'A' ? 'B' : 'A');
        bool oppBidOk = (oppBid.group == oppGroup);
        oppState.bid(oppBidOk, oppBid.amount);
    }

    void updatePut(DicePut put) { myState.useDice(put); }
    void updateSet(DicePut put) { oppState.useDice(put); }
};

// ===== Fallback score (비핫패스) =====
int GameState::calculateScore(const DicePut& put){
    const auto& dice = put.dice;
    switch(put.rule){
        case ONE:   return (int)count(dice.begin(), dice.end(), 1) * 1000;
        case TWO:   return (int)count(dice.begin(), dice.end(), 2) * 2000;
        case THREE: return (int)count(dice.begin(), dice.end(), 3) * 3000;
        case FOUR:  return (int)count(dice.begin(), dice.end(), 4) * 4000;
        case FIVE:  return (int)count(dice.begin(), dice.end(), 5) * 5000;
        case SIX:   return (int)count(dice.begin(), dice.end(), 6) * 6000;
        case CHOICE: return accumulate(dice.begin(), dice.end(), 0) * 1000;
        case FOUR_OF_A_KIND: {
            int cnt[7]={0}; for(int v: dice) cnt[v]++;
            bool ok=false; for(int i=1;i<=6;i++) if(cnt[i]>=4) ok=true;
            return ok? accumulate(dice.begin(), dice.end(), 0)*1000 : 0;
        }
        case FULL_HOUSE: {
            int cnt[7]={0}; for(int v: dice) cnt[v]++;
            bool p=false,t=false;
            for(int i=1;i<=6;i++){ if(cnt[i]==2 || cnt[i]==5) p=true; if(cnt[i]==3 || cnt[i]==5) t=true; }
            return (p&&t)? accumulate(dice.begin(), dice.end(), 0)*1000 : 0;
        }
        case SMALL_STRAIGHT: {
            bool e[7]={0}; for(int v: dice) e[v]=true;
            bool ok=(e[1]&&e[2]&&e[3]&&e[4])||(e[2]&&e[3]&&e[4]&&e[5])||(e[3]&&e[4]&&e[5]&&e[6]);
            return ok?15000:0;
        }
        case LARGE_STRAIGHT: {
            bool e[7]={0}; for(int v: dice) e[v]=true;
            bool ok=(e[1]&&e[2]&&e[3]&&e[4]&&e[5])||(e[2]&&e[3]&&e[4]&&e[5]&&e[6]);
            return ok?30000:0;
        }
        case YACHT: {
            int cnt[7]={0}; for(int v: dice) cnt[v]++;
            for(int i=1;i<=6;i++) if(cnt[i]==5) return 50000;
            return 0;
        }
    }
    return 0;
}

// ===== String helpers =====
static string toString(DiceRule rule) {
    switch (rule) {
        case ONE: return "ONE"; case TWO: return "TWO"; case THREE: return "THREE";
        case FOUR: return "FOUR"; case FIVE: return "FIVE"; case SIX: return "SIX";
        case CHOICE: return "CHOICE"; case FOUR_OF_A_KIND: return "FOUR_OF_A_KIND";
        case FULL_HOUSE: return "FULL_HOUSE"; case SMALL_STRAIGHT: return "SMALL_STRAIGHT";
        case LARGE_STRAIGHT: return "LARGE_STRAIGHT"; case YACHT: return "YACHT";
    }
    return "ONE";
}
static DiceRule fromString(const string& s) {
    if (s=="ONE") return ONE; if (s=="TWO") return TWO; if (s=="THREE") return THREE;
    if (s=="FOUR") return FOUR; if (s=="FIVE") return FIVE; if (s=="SIX") return SIX;
    if (s=="CHOICE") return CHOICE; if (s=="FOUR_OF_A_KIND") return FOUR_OF_A_KIND;
    if (s=="FULL_HOUSE") return FULL_HOUSE; if (s=="SMALL_STRAIGHT") return SMALL_STRAIGHT;
    if (s=="LARGE_STRAIGHT") return LARGE_STRAIGHT; if (s=="YACHT") return YACHT;
    return ONE;
}

// ===== Main: READY 즉시 OK + flush, 이후 로딩/초기화 =====
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // 출력 무버퍼링(선택) — READY 응답 신뢰도 ↑
    setvbuf(stdout, nullptr, _IONBF, 0);

    Game game;
    vector<int> diceA, diceB;
    Bid myBid;
    bool inited=false;
        if (!inited) { // 안전장치
            if (!load_data_bin("data.bin")) { precompute_all_fast(); save_data_bin("data.bin"); }
            build_comb10(); inited=true;
        }
    string line;
    while (getline(cin, line)) {
        if (line.empty()) continue;
        istringstream iss(line);
        string cmd; iss >> cmd;

        if (cmd=="READY") {
            // 1) 즉시 OK 출력 + flush → READY TLE 방지
            cout << "OK\n";
            // 2) 무거운 초기화는 OK 이후에 수행
            if (!inited) {
                // data.bin 시도 → 실패 시 빠른 프리컴퓨트 후 저장
                if (!load_data_bin("data.bin")) {
                    precompute_all_fast();
                    save_data_bin("data.bin");
                }
                build_comb10();
                inited=true;
            }
            continue;
        }

        if (cmd=="ROLL") {
            string A,B; iss >> A >> B;
            diceA.clear(); diceB.clear();
            diceA.reserve(5); diceB.reserve(5);
            for(char c: A) diceA.push_back(c-'0');
            for(char c: B) diceB.push_back(c-'0');

            if (!inited) { // 안전장치
                if (!load_data_bin("data.bin")) { precompute_all_fast(); save_data_bin("data.bin"); }
                build_comb10(); inited=true;
            }

            myBid = game.calculateBid(diceA, diceB);
            cout << "BID " << myBid.group << " " << myBid.amount << "\n";
            continue;
        }

        if (cmd=="GET") {
            char getGroup, oppGroup; int oppScore; iss >> getGroup >> oppGroup >> oppScore;
            game.updateGet(diceA, diceB, myBid, Bid{oppGroup, oppScore}, getGroup);
            continue;
        }

        if (cmd=="SCORE") {
            DicePut put = game.calculatePut();
            game.updatePut(put);
            cout << "PUT " << toString(put.rule) << " ";
            for (int d : put.dice) cout << d;
            cout << "\n";
            continue;
        }

        if (cmd=="SET") {
            string ruleStr, ds; iss >> ruleStr >> ds;
            vector<int> vd; vd.reserve(5);
            for (char c : ds) vd.push_back(c - '0');
            game.updateSet(DicePut{fromString(ruleStr), vd});
            continue;
        }

        if (cmd=="FINISH") break;
    }

    // 정리(선택)
    free_tables();
    return 0;
}
