#include <iostream>
#include <algorithm>

#define FASTIO ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
using namespace std;

int M,N,K;
int arr[100][100];

int ans = 0;
int sizes[101];

int dfs(int x, int y) {
    if (x < 0 || x >= M || y < 0 || y >= N) return 0;
    if (arr[x][y] != 0) return 0;
    int area = 1;
    arr[x][y] = ans;

    area += dfs(x + 1, y);
    area += dfs(x - 1, y);
    area += dfs(x, y + 1);
    area += dfs(x, y - 1);
    return area;
}

void fill_area(int a, int b, int x, int y) {
    for (int i = a; i < x; i++) {
        for (int j = b; j < y; j++) {
            arr[i][j] = -1;
        }
    }
}

int main() {
    FASTIO
    
    cin >> M >> N >> K;

    for(int k = 0; k < K; k++) {
        int a, b, x, y;
        cin >> b >> a >> y >> x;

        fill_area(a, b, x, y);
    }

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            if (arr[i][j] == 0) {
                ans++;
                sizes[ans-1] = dfs(i, j);
            }
        }
    }

    cout << ans << "\n";

    sort(sizes, sizes + ans);
    
    for (int i = 0; i < ans; i++) {
        cout << sizes[i] << " ";
    }
}