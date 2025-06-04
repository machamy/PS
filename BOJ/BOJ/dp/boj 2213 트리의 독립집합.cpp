#include <iostream>
#include <vector>
#include <algorithm>

#define FASTIO ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);


using namespace std;


int N;
int W[10001];
vector<int> edges[10001];

int dp[10001][2]; // dp[node][0] : node 포함 안함, dp[node][1] : node 포함
bool visited[10001];

void dfs(int node){
    visited[node] = true;
    // cout << node << " ";

    dp[node][0] = 0; // node 포함 안함
    dp[node][1] = W[node]; // node 포함

    for(int i = 0; i < edges[node].size(); i++) {
        int next = edges[node][i];
        if(!visited[next]) {
            // cout <<"." << next << " ";
            dfs(next);
            
            // 현재노드 포함 안하는경우
            dp[node][0] += max(dp[next][0], dp[next][1]); 
            // 현재노드 포함하는 경우
            dp[node][1] += dp[next][0]; // 자식 노드 포함 안하는 경우만 가능
        }
    }
    visited[node] = false;
}

void find_ans(int node,bool include,vector<int> &ans) {
    visited[node] = true;
    if(include) {
        ans.push_back(node);
    }

    for(int i = 0; i < edges[node].size(); i++) {
        int next = edges[node][i];
        if(!visited[next]){
            if(include){
                find_ans(next, false,ans); // 현재 노드 포함하는 경우 자식 노드는 포함 안함
            }
            else{
                if(dp[next][0] > dp[next][1]) {
                    find_ans(next, false,ans);
                } else {
                    find_ans(next, true,ans);
                }
            }
        }
    }
}

int main() {
    FASTIO;
    cin >> N;
    for(int i = 1; i <= N; i++) {
        cin >> W[i];
    }
    for(int i = 1; i < N; i++) {
        int u, v;
        cin >> u >> v;
        edges[u].push_back(v);
        edges[v].push_back(u);
    }
    // 리프 노드 중 하나를 루트로 잡고
    // 해당 리프 넣는거랑 안넣는거랑 두 가지 경우에서 dfs를 돌린다.

    dfs(1);
    for(int i = 1; i <= N; i++) {
        visited[i] = false;
    }
    vector<int> ans;
    if(dp[1][0] > dp[1][1]) {
        cout << dp[1][0] << endl;
        find_ans(1, false,ans);
    } else {
        cout << dp[1][1] << endl;
        find_ans(1, true,ans);
    }
    sort(ans.begin(), ans.end());
    for(int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }
    
    cout << endl;
    

    
    return 0;
}