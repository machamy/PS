#include <iostream>
#include <string>
#include <queue>
#include <tuple>
#include <string.h>


using namespace std;

int N, M;
string map[50];
int visited[4][4][50][50];
int di[] = {0, 0, 1, -1};
int dj[] = {1, -1, 0, 0};
int ans = -1;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int si,sj;
    int c0i, c0j;
    int c1i, c1j;
    c0i = c0j = -1;

    memset(visited, -1, sizeof(visited));

    cin >> N >> M;
    for (size_t i = 0; i < N; i++)
    {
        string str;
        cin >> str;
        map[i] = str;
        for (size_t j = 0; j < M; j++)
        {
            if(str[j] == 'S'){
                si = i;
                sj = j;
            }
            else if(str[j] == 'C'){
                if(c0i == -1){
                    c0i = i;
                    c0j = j;
                }
                else{
                    c1i = i;
                    c1j = j;
                }
            }
        }
    }
    

    queue<tuple<int, int, int, int>> q;
    for (size_t dir = 0; dir < 4; dir++)
    {
        q.push({si, sj, dir, 0});
        visited[0][dir][si][sj] = 0;
    }

    while(!q.empty()){
        int i, j, dir, pos_bit;
        tie(i, j, dir, pos_bit) = q.front();
        q.pop();
        int cost = visited[pos_bit][dir][i][j];
        if(pos_bit == 3){
            if(ans == -1)
                ans = cost;
            else
                ans = min(ans, cost);
            break;
        }
        int nxt_cost = cost + 1;
        for (size_t nxt_dir = 0; nxt_dir < 4; nxt_dir++)
        {
            int ni = i + di[nxt_dir];
            int nj = j + dj[nxt_dir];
            int nxt_pos_bit = pos_bit;
            if(ni < 0 || ni >= N || nj < 0 || nj >= M || map[ni][nj] == '#') 
                continue;
            if(dir == nxt_dir)
                continue;
            if(visited[nxt_pos_bit][nxt_dir][ni][nj] != -1)
                continue;
            
            
            if(ni == c0i && nj == c0j)
                nxt_pos_bit |= 1;
            else if(ni == c1i && nj == c1j)
                nxt_pos_bit |= 2;

            visited[nxt_pos_bit][nxt_dir][ni][nj] = nxt_cost;
            q.push({ni, nj, nxt_dir, nxt_pos_bit});
        }
    }
    
    cout << ans << '\n';
    return 0;
}