#include <iostream>
// #include <cstring>

using namespace std;

int MOD = 10'007;

int N;
int dp[60][60];
/*
N개 중에서...
포카드를 1개 이상 뽑는 경우의 수 : 13 C 1 * (N-4 C N-4)
포카드를 2개 이상 뽑는 경우의 수 : 13 C 2 * (N-8 C N-8)


(n+1)C_(r+1) = nC_r + cC_(r+1)
nC0 = nCn = 1
*/

int main(){
    cin >> N;
    if(N < 4){
        cout << 0 << endl;
        return 0;
    }

    // memset(dp,-1,sizeof(int) * 14 * 14 * 14 * 14);
    for(int n=0; n <= 52; n++){
        dp[n][0] = 1; dp[n][n] = 1;
        for(int k = 1; k < n; k++){
            dp[n][k] = (dp[n-1][k-1] + dp[n-1][k]) % MOD;
        }
    }
    int ans = 0;
    for(int i=1; i<=13 && N-4*i>=0; i++) {
        if(i%2 == 1) 
            ans = (ans + dp[52-4*i][N-4*i]*dp[13][i]) % MOD;
        else 
            ans = (ans - (dp[52-4*i][N-4*i]*dp[13][i]) % MOD + MOD) % MOD;
    }

    cout << ans << endl;
    return 0;
}