#include <iostream>
#include <algorithm>

#define FASTIO ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

#define size 100
using namespace std;

int R,C;
int T;
char world[size][size];

int di[4] = {0, 0, -1, 1};
int dj[4] = {-1, 1, 0, 0};

int dfs(int i, int j, int time){
    if(time == T+1)
        return 0;
    
    char tmp = world[i][j];
    // cout << "" << i << " " << j << " " << tmp << "\n";
    if(tmp == '#'){
        return 0;
    }
    int res = 0;
    int Max = 0;

    if(tmp == 'S'){
        res = 1;
    }
    world[i][j] = '.';

    for(int dir = 0; dir < 4; dir++){
        int ni = i + di[dir];
        int nj = j + dj[dir];
        if(ni < 0 || ni >= R || nj < 0 || nj >= C) continue;
        Max = max(Max, dfs(ni, nj, time + 1));
    }

    world[i][j] = tmp;

    return res + Max;
}

int main(){
    FASTIO;

    cin >> R >> C >> T;

    int posi,posj;
    for(int i = 0; i < R; i++){
        string in;
        cin >> in;
        for(int j = 0; j < C; j++){
            world[i][j] = in[j];
            if(world[i][j] == 'G'){
                posi = i;
                posj = j;
                world[i][j] = '.';
            }
        }
    }

    int ans = dfs(posi, posj, 0);
    cout << ans << "\n";
}