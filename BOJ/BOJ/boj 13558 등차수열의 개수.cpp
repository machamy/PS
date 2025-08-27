#include <iostream>

using namespace std;
typedef long long ll;
int N;
int A[100'001];
ll left_cnt[100'001] = {0};
ll right_cnt[100'001] = {0};

ll ans = 0;

/*

세수 a,b,c가 등차수열을 이루는 경우의 수 구하기
b - a = c - b
a + c = 2b


*/
int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin >> N;

    for(int i = 0; i < N; i++) {
        cin >> A[i];
        right_cnt[A[i]]++;
    }


    right_cnt[A[0]]--; // A[0]의 왼쪽값은 없으므로 패스
    for(int i = 1; i < N - 1; i++) { // A[1]부터 시작.
        left_cnt[A[i-1]]++; // A[i-1]을 왼쪽값에 추가
        right_cnt[A[i]]--; // A[i]를 오른쪽값에서 제거 -> L : ~A[i], R : A[i+1]~
        for(int j = 1; j <= 2 * A[i]; j++) { // 2b = a + c
            ans += left_cnt[j] * right_cnt[2 * A[i] - j];
        }
    }

    cout << ans << "\n";
    
    return 0;
}