#include <iostream>
#include <vector>
#include <queue>

#define FASTIO ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
using namespace std;

const int MAX_N = 300000;

int N,M,K,X;
vector<int> adj[MAX_N+1];
int arr[MAX_N+1];
int main(){
    FASTIO;

    cin >> N >> M >> K >> X;
    for(int i=0;i<M;i++){
        int a,b;
        cin >> a >> b;
        adj[a].push_back(b);
        // adj[b].push_back(a);    
    }

    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    pq.push({0,X});
    arr[X] = 0;
    
    while(!pq.empty()){
        int dist = pq.top().first;
        int cur = pq.top().second;
        pq.pop();

        if(arr[cur] < dist) continue;

        for(int i=0;i<adj[cur].size();i++){
            int next = adj[cur][i];
            int cost = dist + 1;

            if(arr[next] == 0 || arr[next] > cost){
                arr[next] = cost;
                pq.push({cost,next});
            }
        }
    }
    bool flag = false;
    for (int i = 1; i <= N; i++)
    {
        if(i == X){
            continue;
        }
        if(arr[i] == K){
            flag = true;
            cout << i << '\n';
        }
    }
    if(!flag){
        cout << -1 << '\n';
    }
}