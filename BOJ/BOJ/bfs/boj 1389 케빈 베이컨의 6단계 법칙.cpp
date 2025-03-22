#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int N,M;
vector<int> adj[101];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N >> M;
    bool visit[101] = {};
    for (int i = 0; i < M; i++)
    {
        int a,b;
        cin >> a >> b;
        if(find(adj[a].begin(),adj[a].end(), a) != adj[a].end()){
            continue;
        }
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    
    int ans_cost = 100000;
    int ans;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j < 101; j++)
        {
            visit[j] = false;
        }
        int total = 0;
        visit[i] = true;
        queue<pair<int,int>> q;
        q.emplace(0,i);
        while(!q.empty()){
            auto [cost, n] = q.front();
            total += cost;
            q.pop();
            for(int nxt : adj[n]){
                if(visit[nxt]) continue;
                visit[nxt] = true;
                q.emplace(cost + 1, nxt);
            }
        }
        // cout << i << " "<< total << endl;
        if(ans_cost > total){
            ans_cost = total;
            ans = i;
        }
    }
    
    cout << ans << endl;
    

}