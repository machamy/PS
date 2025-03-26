#include <iostream>
#include <vector>

using namespace std;

int office[9][9];
int N,M;

// 하 좌 상 우
int di[4] = {1, 0, -1, 0}; 
int dj[4] = {0, -1, 0, 1};

vector<pair<int,int>> cctvs;

int ans = 100;

void watch(int i,int j, int dir){
    dir %= 4;
    while(true){
        int ni = i + di[dir];
        int nj = j + dj[dir];

        if(ni < 0 || ni >= N || nj < 0 || nj >= M) break;;
        if(office[ni][nj] == 6) break;
        if(office[ni][nj] == 0){ //빈땅인경우
            office[ni][nj] = -1;
        }
        i = ni;
        j = nj;
    }
}

void dfs(int idx){
    
    if(idx == cctvs.size()){
        int cnt = 0;
        for (size_t i = 0; i < N; i++)
        {
            for (size_t j = 0; j < M; j++)
            {
                if(office[i][j] == 0){
                    cnt++;
                }
            }
        }
        ans = min(ans,cnt);
        return;
    }
    auto[i,j] = cctvs[idx];

    int prev_state[9][9];
    for (int dir = 0; dir < 4; dir++)
    {
        // cout << idx << " "<< dir << endl;
        for (size_t tmpi = 0; tmpi < N; tmpi++)
        {
            for (size_t tmpj = 0; tmpj < M; tmpj++)
            {
                prev_state[tmpi][tmpj] = office[tmpi][tmpj];
            }
        }

        if(office[i][j] == 1)
            watch(i, j, dir);
        else if(office[i][j] == 2){
            watch(i, j, dir);
            watch(i, j, dir+2);
        }
        else if (office[i][j] == 3){
            watch(i, j, dir);
            watch(i, j, dir + 1);
        }
        else if (office[i][j] == 4){
            watch(i, j, dir);
            watch(i, j, dir + 1);
            watch(i, j, dir + 2); 
        }
        else if (office[i][j] == 5){
            watch(i, j, dir);
            watch(i, j, dir + 1);
            watch(i, j, dir + 2);
            watch(i, j, dir + 3);
        }
        
        dfs(idx + 1);
        for (size_t tmpi = 0; tmpi < N; tmpi++)
        {
            for (size_t tmpj = 0; tmpj < M; tmpj++)
            {
                office[tmpi][tmpj] = prev_state[tmpi][tmpj];
            }
        }
    }
    
}

int main(){
    // ios::sync_with_stdio(false);
    // cin.tie(0);
    // cout.tie(0);

    cin >> N >> M;

    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < M; j++)
        {
            cin >> office[i][j];
            if(office[i][j] > 0 && office[i][j] < 6){
                cctvs.emplace_back(i,j);
            }
        }
    }
    dfs(0);
    cout << ans << endl;

    return 0;
}