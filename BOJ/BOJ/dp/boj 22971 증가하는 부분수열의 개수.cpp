#include <iostream>

#define MOD 998244353

using namespace std;

using ll = long long;

ll ans = 0;

int N;
int arr[5001];
ll dp[5001];


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for (int i = 1; i <= N; i++) {
        cin >> arr[i];
    }

    for (int i = 1; i <= N; i++) {
        dp[i] = 1;
    }

    for (int i = 1; i <= N; i++) {
        for(int j = 1; j < i; j++) {
            if(arr[j] < arr[i]) {
                dp[i] += dp[j];
                dp[i] %= MOD;
            }
        }
    }

    for (int i = 1; i <= N; i++) {
        cout << dp[i] << ' ';
    }
   

    return 0;
}