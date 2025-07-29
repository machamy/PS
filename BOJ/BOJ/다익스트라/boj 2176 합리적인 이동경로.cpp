#include <iostream>
#include <vector>
#include <queue>

using namespace std;

using pii = pair<int,int>;

int N,M;
vector<pii> adj[1001];
int dp[1001];
int dist[1001];
int S = 1,T = 2;


void dijk(int start, int end){
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    fill(dist, dist + N + 1, 1e9);
    pq.push({0, start});
    dist[start] = 0;
    dp[start] = 1;
    while (!pq.empty()) {
        auto [d, cur] = pq.top(); pq.pop();
        if (dist[cur] < d) continue;
        for (auto [nxt, w] : adj[cur]) {
            if (dist[nxt] > d + w) {
                dist[nxt] = d + w;
                pq.push({dist[nxt], nxt});
            }

            if (dist[nxt] < d){
                dp[cur] += dp[nxt];
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        int u,v,w;
        cin >> u >> v >> w;
        adj[u].push_back({v,w});
        adj[v].push_back({u,w});
    }    

    dijk(T,S);

    cout << dp[S] << '\n';

    return 0;
}