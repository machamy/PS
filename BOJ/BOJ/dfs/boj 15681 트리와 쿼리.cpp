#include <iostream>
#include <vector>

using namespace std;

int N,R,Q;
vector<int> edges[100'001];
bool visit[100'001];
int answers[100'001];

int dfs(int node){
    int res = 1;
    // cout << "visit" << node << endl;
    for (int i = 0; i < edges[node].size(); i++)
    {
        int nxt = edges[node][i];
        if(visit[nxt])
            continue;
        visit[nxt] = true;
        res += dfs(nxt);
        visit[nxt] = false;
    }
    answers[node] = res;
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    cin >> N >> R >> Q;
    for(int i = 0; i < N-1; i++){
        int a,b;
        cin >> a >> b;
        edges[a].push_back(b);
        edges[b].push_back(a);
    }

    visit[R] = true;
    dfs(R);

    for(int i = 0; i < Q; i++){
        int n;
        cin >> n;
        cout << answers[n] << "\n";
    }

    return 0;
}