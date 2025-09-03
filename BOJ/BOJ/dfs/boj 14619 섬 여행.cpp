#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int N, M;
int heights[101];

vector<int> adj[101];
int memo[101][501];
int T;

int dfs(int start, int times){
    if (memo[start][times] != -1) {
        return memo[start][times];
    }
    if(times == 0) {
        return heights[start];
    }
    int minHeight = 10000000; // A large number to represent infinity
    for (int next : adj[start]) {
        int height = dfs(next, times - 1);
        minHeight = min(minHeight, height);
    }
    memo[start][times] = minHeight;
    return minHeight;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        cin >> heights[i];
    }
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for(int i = 0; i <= N; i++){
        for(int j = 0; j <= 500; j++){
            memo[i][j] = -1;
        }
    }
    
    cin >> T;
    while (T--) {
        int s,k;
        cin >> s >> k;
        int result = dfs(s, k);
        if (result == 10000000) {
            cout << -1 << '\n';
        } else {
            cout << result << '\n';
        }
    }

    return 0;
}
