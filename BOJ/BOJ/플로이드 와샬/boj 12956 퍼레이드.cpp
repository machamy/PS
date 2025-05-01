#include <vector>
#include <iostream>
#include <tuple>
#include <cstring>


using namespace std;

int INF = (1 << 15);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N, M;
    cin >> N >> M;

    tuple<int,int,int> roads[2000];
    int adj[100][100];
    for(int i = 0; i < N; ++i){
        for(int j = 0; j < N; ++j) {
            adj[i][j] = INF;
        }
    }
    for (int i = 0; i < M; ++i) {
        int u, v, t;
        cin >> u >> v >> t;         
        roads[i] = {u, v, t};
        adj[u][v] = adj[v][u] = t;
    }

    int initial[100][100];

    memcpy(initial, adj, sizeof(adj));

    for (int k = 0; k < N; ++k)
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                initial[i][j] = min(initial[i][j], initial[i][k] + initial[k][j]);

    /* 각 도로를 하나씩 막아 보면서 결과 계산 */
    for (int ban = 0; ban < M; ++ban) {
        int dist[100][100];
        for(int i = 0; i < N; ++i){
            for(int j = 0; j < N; ++j) {
                dist[i][j] = INF;
            }
        }

        for (int i = 0; i < M; ++i) {
            auto [u, v, t] = roads[i];
            dist[u][v] = dist[v][u] = t;
        }
        dist[get<0>(roads[ban])][get<1>(roads[ban])] = INF;
        dist[get<1>(roads[ban])][get<0>(roads[ban])] = INF;

        for (int k = 0; k < N; ++k)
            for (int i = 0; i < N; ++i) {
                for (int j = 0; j < N; ++j) {
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }

        int changed = 0;
        for (int i = 0; i < N; ++i)
            for (int j = i + 1; j < N; ++j)
                if (dist[i][j] != initial[i][j])
                    ++changed;

        cout << changed << ' ';
    }
    return 0;
}
