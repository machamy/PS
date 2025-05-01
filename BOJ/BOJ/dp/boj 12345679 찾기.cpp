#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

const int MOD = 1'000'000'007;
const int TARGET = 2520;

int dp[2][TARGET];

bool chk(int idx, const string& P, const string& S) {
    for (int i = 0; i < P.size(); ++i) {
        if (idx >= S.size()) return false;
        if (P[i] != S[idx]) return false;
        ++idx;
    }
    return true;
}

int main() {
    string P, S;
    cin >> P >> S;

    vector<int> indexes;

    for (int idx = 0; idx < S.size(); ++idx) {
        if (chk(idx, P, S)) {
            indexes.push_back(idx + 1);
        }
    }

    memset(dp, 0, sizeof(dp));

    for (int i = 0; i < indexes.size(); ++i) {
        int flag = i % 2;
        int prev = (i + 1) % 2;

        for (int j = 0; j < TARGET; ++j) {
            dp[flag][j] = dp[prev][j];
        }

        int mod = indexes[i] % TARGET;
        dp[flag][mod] = (dp[flag][mod] + 1) % MOD;

        for (int j = 0; j < TARGET; ++j) {
            if (dp[prev][j]) {
                int n = (1LL * j * indexes[i]) % TARGET;
                dp[flag][n] = (dp[flag][n] + dp[prev][j]) % MOD;
            }
        }
    }

    cout << dp[int((indexes.size() % 2 == 0))][0] << '\n';

    return 0;
}
