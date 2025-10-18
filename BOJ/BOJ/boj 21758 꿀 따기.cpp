#include <iostream>



using namespace std;


int N;
int honey[100'001];
int prefixSum[100'001];
// int suffixSum[100'001];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;

    for(int i = 1; i <= N; i++) {
        cin >> honey[i];
    }
    for(int i = 1; i <= N; i++) {
        prefixSum[i] = prefixSum[i - 1] + honey[i];
    }
    // for(int i = N - 2; i >= 0; i--) {
    //     suffixSum[i] = suffixSum[i + 1] + honey[i];
    // }

    /*
    세가지 경우의 수.
    1. 왼쪽에서 2개
    2. 오른쪽에서 2개
    3. 양쪽 하나씩

    1. 왼쪽에서 2개 / 오른쪽에서 두개.
    당연히 꿀통은 반대편 끝임.
    벌 한마리도 한쪽 끝.
    나머지 하나의 위치를 찾아보자

    */

    int ans = 0;
    // 1. 왼쪽에서 2개
    // i : 벌 B
    // N : 벌통
    
    for(int i = 2; i < N; i++) {
        // 벌 A : prefixSum[N] - honey[1] (첫 장소를 제외하고 다 먹음)
        // 벌 B : prefixSum[N] - prefixSum[i] (i 장소를 제외하고 오른쪽 다 먹음)
        // 벌 A에서 B 부분 빼기 : - honey[i]
        int h = prefixSum[N] - honey[1] + (prefixSum[N] - prefixSum[i]) - honey[i];
        // cout << "[left] i : " << i << " h : " << h << "\n";
        ans = max(ans, h);
    }
    // 2. 오른쪽에서 2개
    // i : 벌 B
    // 1 : 벌통
    for(int i = N-1; i > 1; i--) {
        // 벌 A : prefixSum[N] - honey[N] = prefixSum[N-1] (끝 장소를 제외하고 다 먹음)
        // 벌 B : prefixSum[i - 1] (i 장소를 제외하고 왼쪽 다 먹음)
        // 벌 A에서 B 부분 빼기 : - honey[i]
        int h = prefixSum[N-1] + (prefixSum[i - 1]) - honey[i];
        // cout << "[right] i : " << i << " h : " << h << "\n";
        ans = max(ans, h);
    }

    // 3. 양쪽 하나씩
    // i : 벌통
    for(int i = 2; i < N; i++) {
        // 벌 A : prefixSum[i] - honey[1] (i 왼쪽 다 먹음)
        // 벌 B : prefixSum[N - 1] - prefixSum[i - 1] (i 오른쪽 다 먹음)
        int h = prefixSum[i] - honey[1] + (prefixSum[N - 1] - prefixSum[i - 1]);
        // cout << "[mid] i : " << i << " h : " << h << "\n";
        ans = max(ans, h);
    }

    cout << ans << "\n";
    return 0;
}