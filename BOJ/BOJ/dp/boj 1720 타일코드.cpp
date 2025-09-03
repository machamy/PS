#include <iostream>

using namespace std;

int N;

/*
    1. 평범한 타일링 문제처럼 끝까지 했을때의 경우의 수를 구함.
    2. 전체 경우의수 - 대칭인 경우의 수 / 2 = 대칭이 아닌 경우의 수
    3. 정답 :   대칭이 아닌 경우의 수 + 대칭인 경우의 수

 */


 /*
 1 : 1
 2 : 3
 3 : 5
 4 : 8
 
 8 : 98
 16 : 22016
 */
int dp[31];

int main(){
    cin >> N;

    dp[0] = 1;
    dp[1] = 1;
    for(int i = 2; i <= N; i++){
        // 세로 한줄
        dp[i] = dp[i - 1];
        // 가로 두줄
        dp[i] += dp[i - 2];
        // 네모
        dp[i] += dp[i - 2];
    }

    int symetric_count = 0;
    if(N % 2 == 0){
        // 중앙에서 한칸 비우고 '네모' '가로두줄'
        symetric_count = dp[N / 2 - 1] * 2;
        // 정 중앙까지의 경우의 수
        symetric_count += dp[N / 2];
    } else {
        // 중앙에서 한칸 비우고 '세로'
        symetric_count = dp[N / 2];
    }
    int asymetric_count = dp[N] - symetric_count;
    int result = asymetric_count / 2 + symetric_count;
    // cout << "all :" << dp[N] << endl;
    // cout << "symetric :" << symetric_count << endl;
    // cout << "asymetric :" << asymetric_count << endl;
    // cout << "result :" << result << endl;
    cout << result << endl;

    return 0;
}