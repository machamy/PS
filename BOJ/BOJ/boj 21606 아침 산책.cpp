#include <iostream>
#include <vector>

#define MAX_NODE 2*100000

using namespace std;


bool visited[MAX_NODE+1];
bool isInside[MAX_NODE+1];
vector<int> adj[MAX_NODE+1];

int N;

int dfs(int node){
    int cnt = 0;
    // cout << "dfs "<< node << endl;
    visited[node] = true;
    for(int nxt: adj[node]){
        if(visited[nxt])
            continue;
        if(isInside[nxt]){
            cnt += 1;
        }else{
            cnt += dfs(nxt);
        }
    }
    return cnt;
}


int main(){
    cin >> N;

    for(int i = 0; i < N; i++){
        char in;
        cin >> in;
        isInside[i+1] = in == '1';
    }

    int attaches = 0;
    for(int i = 0; i < N-1;i++){
        int a,b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
        if(isInside[a] && isInside[b]){
            attaches++;
        }
    }
    int res = 0;
    for(int i = 1; i <= N; i++){
        if(isInside[i] || visited[i])
            continue;
        int cnt = dfs(i);
        res += (cnt * (cnt-1)); // cnt 가 1이거나 0이면 경우의수도 0개
    }
    
    cout << 2 * attaches + res << endl;

    return 0;
}