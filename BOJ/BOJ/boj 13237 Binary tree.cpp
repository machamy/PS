#include <iostream>
#include <vector>

using namespace std;


int N;
int parent[21];
vector<int> child[21];
int ans[21];
int root;

void dfs(int node, int level){
    ans[node] = level;
    for(int nxt : child[node]){
        dfs(nxt,level+1);
    }
}

int main(){
    cin >> N;

    for(int i = 1; i <= N; i++){
        cin >> parent[i];
        if(parent[i] == -1){
            root = i;
        }
        else{
            child[parent[i]].push_back(i);
        }
    }

    dfs(root,0);

    for(int i = 1; i <= N; i++){
        cout << ans[i] << "\n";
    }
}