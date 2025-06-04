#include <iostream>

using namespace std;

int N,M;
int A[500'001];
int main(){
     cin.tie(0);
    ios::sync_with_stdio(0);

    cin >> N >> M;
    for(int i=0; i<N; i++){
        cin >> A[i];
    }
    int l = 0, r = 0;
    int sum = 0;
    int ans = 0;
    while (r < N) {
        sum += A[r++];
        // cout << "sum + r: " << sum << "\n";
        while (sum > M) {
            sum -= A[l++];
            // cout << "sum - l: " << sum << "\n";
        }
        ans = max(ans,sum);
    }
    cout << ans << "\n";
    return 0;
}