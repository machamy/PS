#include <iostream>

#define MOD 1'000'000'007

using namespace std;



int N,M;
// N : 알파벳간의 거리
// M : 비번 길이 

int dp[10001][26];
int main() {
    cin >> N >> M;
    
    // O(26)
    for(int i = 0; i < 26; i++) {
        dp[1][i] = 1; 
    }
    
    // O(M * 26 * 26)
    for(int i = 2; i <= M; i++) {
        for(int j = 0; j < 26; j++) {
            for(int k = 0; k < 26; k++) {
                if(abs(j-k) >= N) {
                    dp[i][k] = (dp[i][k] + dp[i-1][j]) % MOD;
                }
            }
        }
    }

    int ans = 0;
    for(int i = 0; i < 26; i++) {
        ans = (ans + dp[M][i]) % MOD;
    }
    cout << ans << endl;
    return 0;
}