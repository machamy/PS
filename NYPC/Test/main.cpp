// g++ -std=c++20 -O2 -pipe -static -s mushroom_ai.cpp -o mushroom_ai
#include <bits/stdc++.h>
using namespace std;

constexpr int R = 10;
constexpr int C = 17;

struct Rect { int r1, c1, r2, c2; };

class Game {
    /* ------------------------------------------------------------------ */
    /*  상태                                                               */
    /* ------------------------------------------------------------------ */
    vector<vector<int>> board;           // 버섯 숫자(0‑9), 0 이면 제거
    vector<vector<int>> owner;           // 0: 미점령, 1: 내 것, 2: 상대 것
    bool first = false;                  // 선공 여부

    /* ------------------------------------------------------------------ */
    /*  헬퍼: 사각형 유효 여부(합 10 & 네 변에 최소 1칸)                  */
    /* ------------------------------------------------------------------ */
    static bool isValid(const vector<vector<int>>& B,
                        int r1,int c1,int r2,int c2)
    {
        int sum = 0;
        bool top=0,bot=0,left=0,right=0;

        for(int r=r1;r<=r2;++r)
            for(int c=c1;c<=c2;++c)
                if(B[r][c]){
                    sum += B[r][c];
                    if(r==r1) top  =1;
                    if(r==r2) bot  =1;
                    if(c==c1) left =1;
                    if(c==c2) right=1;
                }
        return sum==10 && top && bot && left && right;
    }

    /* ------------------------------------------------------------------ */
    /*  헬퍼: 사각형 점령 시 새로 얻는 칸 수                              */
    /* ------------------------------------------------------------------ */
    static int gainIfCaptured(const Rect& R,
                              const vector<vector<int>>& own,
                              int who)        // 1 = 나, 2 = 상대
    {
        int g=0;
        for(int r=R.r1;r<=R.r2;++r)
            for(int c=R.c1;c<=R.c2;++c)
                if(own[r][c]!=who) ++g;
        return g;
    }

    /* ------------------------------------------------------------------ */
    /*  헬퍼: 현 보드에서 모든 유효 사각형 나열                           */
    /* ------------------------------------------------------------------ */
    static vector<Rect> listValid(const vector<vector<int>>& B)
    {
        vector<Rect> v;
        for(int r1=0;r1<R;++r1) for(int c1=0;c1<C;++c1)
        for(int r2=r1;r2<R;++r2) for(int c2=c1;c2<C;++c2)
            if(isValid(B,r1,c1,r2,c2)) v.push_back({r1,c1,r2,c2});
        return v;
    }

public:
    Game() = default;
    Game(const vector<vector<int>>& b,bool f)
        : board(b), owner(R,vector<int>(C,0)), first(f) {}

    /* ------------------------------------------------------------------ */
    /*  핵심: 내 턴에 둘 수 계산                                           */
    /* ------------------------------------------------------------------ */
    vector<int> calculateMove(int /*myTime*/, int /*oppTime*/)
    {
        /* --- 현 상태에서 가능한 직사각형 --- */
        auto valids = listValid(board);
        if(valids.empty()) return {-1,-1,-1,-1};

        /* 후보를 gain 기준 상위 N 개로 줄임 */
        struct Info{ Rect R; int gain; };
        vector<Info> cand;
        for(auto& R:valids){
            int g = gainIfCaptured(R,owner,1);
            if(g>0) cand.push_back({R,g});
        }
        if(cand.empty()) return {-1,-1,-1,-1};

        sort(cand.begin(),cand.end(),
            [](auto&a,auto&b){ return a.gain>b.gain; });

        const int K = min<int>(40,cand.size());          // 상위 40개만

        /* --------- 평가 파라미터 --------- */
        const double BETA  = 0.80;   // 상대 즉시 이득 가중치
        const double GAMMA = 0.20;   // 상대 남은 기회 수 가중치
        const double DELTA = 0.50;   // 내가 다시 되받는 이득 가중치

        /* --------- 탐색 --------- */
        double bestScore = -1e9;
        Rect   bestRect  = {-1,-1,-1,-1};

        for(int i=0;i<K;++i){
            Rect R = cand[i].R;
            int  myGain = cand[i].gain;

            /* --- 내 수 적용 --- */
            auto b2 = board;
            auto o2 = owner;
            for(int r=R.r1;r<=R.r2;++r)
                for(int c=R.c1;c<=R.c2;++c){
                    b2[r][c]=0; o2[r][c]=1;
                }

            /* --- 상대 가능한 사각형 --- */
            auto oppV   = listValid(b2);
            int  oppCnt = (int)oppV.size();

            int  oppBestGain = 0;
            Rect oppBestRect{};
            for(auto& S:oppV){
                int g = gainIfCaptured(S,o2,2);
                if(g>oppBestGain){
                    oppBestGain = g;
                    oppBestRect = S;
                }
            }

            /* --- 깊이‑2: 상대 best 수 이후 내 재반격 --- */
            int reGain = 0;
            if(oppBestGain>0){
                /* 상대 수 적용 */
                for(int r=oppBestRect.r1;r<=oppBestRect.r2;++r)
                    for(int c=oppBestRect.c1;c<=oppBestRect.c2;++c){
                        b2[r][c]=0; o2[r][c]=2;
                    }
                for(auto& T:listValid(b2))
                    reGain = max(reGain, gainIfCaptured(T,o2,1));
            }

            double score = myGain - BETA*oppBestGain
                                   - GAMMA*oppCnt
                                   + DELTA*reGain;

            if(score > bestScore ||
              (fabs(score-bestScore)<1e-9 &&
               tie(R.r1,R.c1,R.r2,R.c2) <
               tie(bestRect.r1,bestRect.c1,bestRect.r2,bestRect.c2))){
                bestScore = score;
                bestRect  = R;
            }
        }

        /* --- 패스 여부 --- */
        if(bestScore < 1.0) return {-1,-1,-1,-1};
        return {bestRect.r1,bestRect.c1,bestRect.r2,bestRect.c2};
    }

    /* ------------------------------------------------------------------ */
    /*  보드 갱신                                                          */
    /* ------------------------------------------------------------------ */
    void updateMove(int r1,int c1,int r2,int c2,bool mine)
    {
        if(r1==-1) return;                       // 패스
        int mark = mine ? 1 : 2;
        for(int r=r1;r<=r2;++r)
            for(int c=c1;c<=c2;++c){
                board[r][c]=0;
                owner[r][c]=mark;
            }
    }
    void updateOpponentAction(const vector<int>& a,int /*time*/){
        updateMove(a[0],a[1],a[2],a[3],false);
    }
};

/* ====================================================================== */
/*  메인                                                                  */
/* ====================================================================== */
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    Game game;
    bool first = false;
    string line;

    while(getline(cin,line)){
        if(line.empty()) continue;
        istringstream iss(line);
        string cmd; iss>>cmd;

        if(cmd=="READY"){
            string turn; iss>>turn; first = (turn=="FIRST");
            cout<<"OK\n"<<flush;
        }
        else if(cmd=="INIT"){
            vector<vector<int>> b(R,vector<int>(C));
            for(int r=0;r<R;++r){
                string row; iss>>row;
                for(int c=0;c<C;++c) b[r][c]=row[c]-'0';
            }
            game = Game(b,first);
        }
        else if(cmd=="TIME"){
            int myT,oppT; iss>>myT>>oppT;
            auto mv = game.calculateMove(myT,oppT);
            game.updateMove(mv[0],mv[1],mv[2],mv[3],true);
            cout<<mv[0]<<" "<<mv[1]<<" "<<mv[2]<<" "<<mv[3]<<'\n'<<flush;
        }
        else if(cmd=="OPP"){
            int r1,c1,r2,c2,t; iss>>r1>>c1>>r2>>c2>>t;
            game.updateOpponentAction({r1,c1,r2,c2},t);
        }
        else if(cmd=="FINISH") break;
    }
    return 0;
}
