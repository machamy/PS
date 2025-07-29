// N = int(input())
// arr = list(map(int, input().split()))
// prefix_sum = [0] * (N + 1)
// for i in range(1, N + 1):
//     prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

// def s(i,k):
//     return prefix_sum[i + k - 1] - prefix_sum[i - 1]

// """

// """

// ans_k = -1
// ans_minSum = float('inf')


// for k in range(1, N//2 + 1):
//     sums = [[s(i,k), i, i + k - 1] for i in range(1, N - k + 2)]
//     sums.sort()
//     for i in range(len(sums)):
//         for j in range(i + 1, len(sums)):
//             if sums[i][2] < sums[j][1] or sums[j][2] < sums[i][1]:
//                 if abs(sums[i][0] - sums[j][0]) <= ans_minSum:
//                     ans_minSum = abs(sums[i][0] - sums[j][0])
//                     ans_k = k  
//                 break

// print(ans_k)
// print(ans_minSum)

#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
#include <climits>

using namespace std;
using ll = long long;

int N;
int arr[3001];
ll prefix_sum[3001];

ll s(int i, int k) {
    return prefix_sum[i + k - 1] - prefix_sum[i - 1];
}

int main() {
    cin >> N;
    for (int i = 1; i <= N; i++) {
        cin >> arr[i];
        prefix_sum[i] = prefix_sum[i - 1] + arr[i];
    }

    ll ans_k = -1;
    ll ans_minSum = LLONG_MAX;

    for (int k = 1; k <= N / 2; k++) {
        vector<tuple<ll,int,int>> sums;
        for (int i = 1; i <= N - k + 1; i++) {
            sums.push_back({s(i, k), i, i + k - 1});
        }
        sort(sums.begin(), sums.end());

        for (int i = 0; i < sums.size(); i++) {
            for (int j = i + 1; j < sums.size(); j++) {
                if (get<2>(sums[i]) < get<1>(sums[j]) || get<2>(sums[j]) < get<1>(sums[i])) {
                    if (abs(get<0>(sums[i]) - get<0>(sums[j])) <= ans_minSum) {
                        ans_minSum = abs(get<0>(sums[i]) - get<0>(sums[j]));
                        ans_k = k;
                    }
                    break; // No need to check further pairs for this k
                }
            }
        }
    }

    cout << ans_k << endl;
    cout << ans_minSum << endl;

    return 0;
}