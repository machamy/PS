#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

int H,W;

string world[500];
int visited[500][500];

// 5~7 : 우측으로 이동하는 경우
int di[8] = {-1,  0,  1, 1, -1, -1, 0, 1};
int dj[8] = {-1, -1, -1, 0,  0,  1, 1, 1};


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> H >> W;
    for(int i = 0; i < H; i++){
        cin >> world[i];
    }

    int start_i, start_j;
    for(int i = 0; i < H; i++){
        for(int j = 0; j < W; j++){
            visited[i][j] = -1;
            if(world[i][j] == 'K'){
                start_i = i;
                start_j = j;
            }
        }
    }

    priority_queue<tuple<int,int,int>,vector<tuple<int,int,int>>,greater<tuple<int,int,int>>> q;
    q.push({0, start_i, start_j});
    visited[start_i][start_j] = 0;

    int ans = -1;

    while(!q.empty()){
        auto [dist, i, j] = q.top();
        q.pop();
        if(ans != -1 && dist > ans) continue; // 이미 더 짧은 경로가 발견된 경우

        for(int d = 0; d < 8; d++){
            int ni = i + di[d];
            int nj = j + dj[d];
            int n_dist = dist + (d < 5 ? 1 : 0); // 5~7는 우측으로 이동하는 경우

            if(ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
            if(world[ni][nj] == '#') continue;
            if(world[ni][nj] == '*') {
                if(ans == -1 || n_dist < ans) {
                    ans = n_dist; // 목표 지점에 도달한 경우
                    visited[ni][nj] = n_dist; // 기록
                }
                continue;
            }
            if(visited[ni][nj] == -1 || visited[ni][nj] > n_dist){
                visited[ni][nj] = n_dist;
                q.push({n_dist, ni, nj}); 
            }
        }
    }

// #ifndef ONLINE_JUDGE
//     for(int i = 0; i < H; i++){
//         for(int j = 0; j < W; j++){
//             cout << visited[i][j] << " ";
//         }
//         cout << "\n";
//     }
// #endif

    cout << ans << "\n";
    return 0;
}