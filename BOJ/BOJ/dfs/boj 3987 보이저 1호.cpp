#include <iostream>
#include <cstring>

#define FASTIO ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);


using namespace std;

int N,M;
string space[501];


#define UP 0
#define RIGHT 1
#define DOWN 2
#define LEFT 3
// U R D L
int di[4] = {-1,0,1,0};
int dj[4] = {0,1,0,-1};

int visited[501][501][4];

int PR,PC;
int ans_dir;
int ans = 0;

string getdir(int d){
    if(d == UP) return "U";
    else if(d == RIGHT) return "R";
    else if(d == DOWN) return "D";
    else if(d == LEFT) return "L";
    return "ERR";
}

int changedir(char c, int d){
    if(c == '/'){
        if(d == UP) return RIGHT;
        else if(d == RIGHT) return UP;
        else if(d == DOWN) return LEFT;
        else if(d == LEFT) return DOWN;
    }else if(c == '\\'){
        if(d == UP) return LEFT;
        else if(d == RIGHT) return DOWN;
        else if(d == DOWN) return RIGHT;
        else if(d == LEFT) return UP;
    }
    return -1;
}

int go(int i, int j, int d, int cnt = 1){
    if(visited[i][j][d]) 
        return -1;
    visited[i][j][d] = 1;
    
    int ni = i + di[d];
    int nj = j + dj[d];
    
    if(ni < 0 || ni >= N || nj < 0 || nj >= M) 
        return cnt;
    auto &c = space[ni][nj];
    if(c == '.'){
        return go(ni, nj, d, cnt + 1);
    }else if (c == 'C'){
        return cnt;
    }else if (c == '/'){
        return go(ni, nj, changedir('/', d), cnt + 1);
    }else{
        return go(ni, nj, changedir('\\', d), cnt + 1);
    }
}

int main() {
    FASTIO

    cin >> N >> M;
    for(int i=0; i<N; i++){
        cin >> space[i];
    }
    
    cin >> PR >> PC;
    PR--, PC--;
    for(int i=0; i<4; i++){
        int result = go(PR, PC, i);
        if(result == -1) {
            cout << getdir(i) << endl;
            cout << "Voyager" << endl;
            return 0;
        }
        if(result > ans) {
            ans = result;
            ans_dir = i;
        }
        memset(visited, 0, sizeof(visited));
    }
    cout << getdir(ans_dir) << endl;
    cout << ans << endl;
    return 0;
}