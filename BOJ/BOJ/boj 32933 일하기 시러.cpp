#include <iostream>
#include <cmath>
#include <queue>
#include <vector>

using namespace std;

typedef long long ll;

struct Fruit{
    int A;
    int B;
    int C;
    double efficiency;
};

/*
1 10 3
5 5 8
2 2 5
3 10 11

0~3 : 11점
3~5 : 5점
5~8 : 11점
8~10: 5점
-> 32점 
*/

int N, M, K;
Fruit fruits[101];
int dp[51][101];

int main()
{
    std::ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M >> K;
    for(int i = 0; i < K; i++){
        Fruit& fruit = fruits[i];
        cin >> fruit.A >> fruit.B >> fruit.C;
        if(fruit.B > fruit.A){
            // 기다리지 않고 새로심으면 되니까 바꿔주기
            fruit.B = fruit.A;
        }
    }

    /*
        dp[day][f]
        day일의 f가 심겨져있을 경우 최대값

        dp[day][f] = Max dp[day-f.A][prev_f] for prev_f != f,
                         dp[day-f.b][prev_f] for prev_f == f
    */
    for(int day = 0; day <= M; day++){
        // cout << "Day " << day << endl;
        for(int f_idx = 0; f_idx < K; f_idx++){
            Fruit& to_plant = fruits[f_idx];
            if(day>0){
                dp[day][f_idx] = dp[day-1][f_idx];
            }
            for(int prev_idx = 0; prev_idx < K; prev_idx++){
                if(prev_idx == f_idx){
                    if(day-to_plant.B < 0 || day-to_plant.A < 0 || dp[day-to_plant.B][f_idx] < 0){
                        continue;
                    }
                    // 이미 같은 열매가 심어져 있음
                    dp[day][f_idx] = max(dp[day][f_idx], dp[day-to_plant.B][prev_idx] + to_plant.C);
                }else{
                    if(day - to_plant.A < 0){
                        continue;
                    }
                    // 다른 열매(새로심어야함)
                    // cout << "prev : " << prev_idx << endl;
                    dp[day][f_idx] = max(dp[day][f_idx], dp[day-to_plant.A][prev_idx] + to_plant.C);
                }
            }

            // cout << f_idx << " : " << dp[day][f_idx] << endl;
        }
    }
    int ans = 0;
    for(int f_idx = 0; f_idx < K; f_idx++){
        ans = max(dp[M][f_idx],ans);
    }

    cout << ans * N << endl;
}