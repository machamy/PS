#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int N,M;
vector<int> adj[200'001];
int dist[200'001];
bool cached[200'001];

bool can_be_cheated(int v){
    int cnt = 0;
    for(int next : adj[v]){
        if(dist[next] != -1) cnt++;
    }
    // cout << "  can_be_cheated " << v << " " << cnt << "/" << adj[v].size() << "\n";
    return cnt * 2 >= (int)adj[v].size();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    for(int i = 1; i <= N; i++){
        int v;
        while(true){
            cin >> v;
            if(v == 0) break;
            adj[i].push_back(v);
        }
    }

    fill(dist, dist + N + 1, -1);

    bool changed = true;
    queue<int> dirty;
    
    cin >> M;
    for(int i = 0; i < M; i++){
        int v;
        cin >> v;
        dist[v] = 0;
        dirty.push(v);
    }
    int step = 0;
    while(changed){
        changed = false;
        int size = dirty.size();
        // cout << "step " << step << " size " << size << "\n";
        for(int _ = 0; _ < size; _++){
            int cur = dirty.front();
            dirty.pop();

            for(int next : adj[cur]){
                if(dist[next] != -1) continue;
                cached[next] = can_be_cheated(next);
                // cout << "  cached " << next << "\n";
            }
            dirty.push(cur);
        }

        for(int _ = 0; _ < size; _++){
            int cur = dirty.front();
            dirty.pop();

            for(int next : adj[cur]){
                if(dist[next] != -1) continue;
                if(cached[next]){
                    dist[next] = step + 1;
                    changed = true;
                    dirty.push(next);
                }
            }
        }
        step++;
        fill(cached, cached + N + 1, false);
    }

    for(int i = 1; i <= N; i++){
        cout << dist[i] << " ";
    }
    cout << "\n";

    return 0;
}