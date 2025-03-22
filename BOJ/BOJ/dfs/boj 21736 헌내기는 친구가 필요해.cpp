#include <iostream>

using namespace std;

int N,M;

int D4i[] = {1,0,-1,0};
int D4j[] = {0,1,0,-1};

bool visit[601][601];
string world[601];

int dfs(int i,int j){
    int res = 0;
    if(i < 0 || i >= N || j < 0 || j >= M)
        return 0;
    if(visit[i][j] || world[i][j] == 'X')
        return 0;
    visit[i][j] = true;
    if(world[i][j] == 'P'){
        res += 1;
    }
    // cout << i << " " << j << " : "<< res << endl;
    for (int k = 0; k < 4; k++)
    {
        res += dfs(i+D4i[k],j+D4j[k]);
    }
    
    return res;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int y = -1,x;
    cin >> N >> M;

    for(int i = 0; i < N; i++){
        cin >> world[i];
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j ++){
            if(world[i][j] == 'I'){
                y = i;
                x = j;
                break;
            }
        }
        if(y != -1)
            break;
    }
    
    int res = dfs(y,x);
    if(res){
        cout << res << endl;
    }else{
        cout << "TT" << endl;
    }

    return 0;
}