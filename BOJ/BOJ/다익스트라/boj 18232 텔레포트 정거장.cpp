#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#define FASTIO ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)

using namespace std;
using pii = pair<int,int>;
const int MAX_N = 300'000;

int N,M;
int S,E;

vector<int> adj[MAX_N+1];

int dp[MAX_N+1];

int main() {
    FASTIO;
    
    memset(dp,-1,sizeof(dp));

    cin >> N >> M;
    cin >> S >> E;

    for(int i = 0; i < M; i++) {
        int a,b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }


    dp[S] = 0;
    priority_queue<pii,vector<pii>, greater<pii>> pq;
    pq.push({0,S});
    while(!pq.empty()){
        int cost = pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        
        if(dp[cur] < cost) continue;
        int nextCost = cost + 1;
        int next = cur + 1;
        if (next <= N && (dp[next] == -1 || nextCost < dp[next])) {
            dp[next] = nextCost;
            pq.push({nextCost,next});
        }
        next = cur - 1;
        if (next <= N && (dp[next] == -1 || nextCost < dp[next])) {
            dp[next] = nextCost;
            pq.push({nextCost,next});
        }
        for (int next : adj[cur]) {
            if(dp[next] == -1 || nextCost < dp[next]) {
                dp[next] = nextCost;
                pq.push({nextCost,next});
            }
        }
    }
    // print dp
    // for(int i = 1; i <= N; i++) {
    //     cout << dp[i] << " ";
    // }
    cout << dp[E] << endl;

    return 0;
}   