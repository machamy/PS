#include <iostream>
#include <vector>
#include <string>
#include <bitset>

#define BIT_WITDH 32

using namespace std;

typedef long long ll;

bitset<2000> bits[2000];

// int get_cnt(int a, int b){
//     int cnt = 0;
//     for (int i = 0; i < BIT_WITDH; ++i) {
//         cnt += __builtin_popcount(bits[a][i] & bits[b][i]);
//     }
//     return cnt;
// };
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        string adj;
        cin >> adj;
        bits[i] = bitset<2000>(adj);
    }
    int Q;
    cin >> Q;

    while (Q--) {
        int a, b;
        cin >> a >> b;
        --a, --b;
        int res = (bits[a] & bits[b]).count();
        cout << res << '\n';
    }

    return 0;
}
