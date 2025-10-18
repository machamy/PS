#include <iostream>
#include <algorithm>

using namespace std;

constexpr int Y0 = 1900;
constexpr int TARGET_Y = 2001, TARGET_M = 11, TARGET_D = 4;

// year, month, day
// 0 : 짐, 1 : 이김
int dp[102][13][32];

bool is_yoon(int year){
    if(year % 400 == 0) return true;
    if(year % 100 == 0) return false;
    if(year % 4 == 0) return true;
    return false;
}

bool solve(){
    int Y, M, D;
    cin >> Y >> M >> D;
    return dp[Y-Y0][M][D] == 1;
}

int month_day(int y, int m){
    static int month_days[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if(m == 2 && is_yoon(y)) return 29;
    return month_days[m];
}

void next_date(int &y, int &m, int &d){
    int md = month_day(y, m);
    d++;
    if(d > md){
        d = 1;
        m++;
        if(m > 12){
            m = 1;
            y++;
        }
    }
}

void prev_date(int &y, int &m, int &d){
    d--;
    if(d < 1){
        m--;
        if(m < 1){
            m = 12;
            y--;
        }
        d = month_day(y, m);
    }
}

bool next_month_possible(int &y, int &m, int &d){
    int ny = y, nm = m, nd = d;
    nm++;
    if(nm > 12){
        nm = 1;
        ny++;
    }
    int md = month_day(ny, nm);
    if(nd <= md){
        // 다음달에 같은 날짜가 존재
        y = ny; m = nm; d = nd;
        return true;
    }
    return false;
}

void compute(){
    fill(&dp[0][0][0], &dp[101][12][32], -1);

    // 목표 일자에서 시작하면, 선플레이어는 당연하 진다.
    dp[TARGET_Y-Y0][TARGET_M][TARGET_D] = 0;
    int y = TARGET_Y, m = TARGET_M, d = TARGET_D;
    while(y >= Y0 && m >= 1 && d >= 1){
        // 이전 날짜로 이동. 1900.1.1 까지 탐색
        prev_date(y, m, d);
       
        bool win = false;
        // 1. 다음날 체크
        int ny = y, nm = m, nd = d;
        next_date(ny, nm, nd);
        if(dp[ny-Y0][nm][nd] == 0){
            // 상대방이 지는 곳으로 갈 수 있으면 이김
            win = true;
        }
        // 2. 다음달 체크
        ny = y, nm = m, nd = d;
        if(next_month_possible(ny, nm, nd)){
            if(dp[ny-Y0][nm][nd] == 0){
                win = true;
            }
        }

        if(win) dp[y-Y0][m][d] = 1;
        else dp[y-Y0][m][d] = 0;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    compute();
  
    int T;
    cin >> T;
    while(T--){
        if(solve()) cout << "YES\n";
        else cout << "NO\n";
    }

    return 0;
}