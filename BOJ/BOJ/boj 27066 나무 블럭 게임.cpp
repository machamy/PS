#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

int N;
int A[100'001];

/*


1 2 3 4 -> 2
1.5 3 4 -> 3
1 2 3 -> 2
1 2 -> 1.5


1 2 3 4 5 6 7 8 9   9개 -> 5번째
1.5 3 4 5 6 7 8 9   8개 -> 4번째
2 4 5 6 7 8 9       7개 -> 4번째
2.5 5 6 7 8 9       6개 -> 3번째
*/
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    int total = 0;
    for(int i = 1; i <= N; i++){
        cin >> A[i];
        total += A[i];
    }

    sort(A+1,A+N+1);

    long double ans = max(total/(long double)N,(long double)A[N-1]);

    cout << fixed << setprecision(7);

    cout << ans << "\n";
}