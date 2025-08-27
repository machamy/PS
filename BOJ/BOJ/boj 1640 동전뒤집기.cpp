#include <iostream>
#include <queue>
#include <vector>
#include <utility>

using namespace std;
int N,M;
char world[1001][1001];
int dis[1001][1001];

// true : 홀수
// false : 짝수
int vertical;
int horizontal;

void init(){
    int vertical_sum[1001] = {0};
    for (int i = 0; i < N; i++) {
        int horizontal_sum = 0;
        for (int j = 0; j < M; j++) {
            horizontal_sum += world[i][j];
            vertical_sum[j] += world[i][j];
        }
        if (horizontal_sum & 1) {
            horizontal++;
        }

    }
    for (int i = 0; i < M; i++) {
        if (vertical_sum[i] & 1) {
            vertical++;
        }
    }
}


int main() {

    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> world[i][j];
        }
    }

    for(int i = 0; i <= N; i++) {
        for (int j = 0; j <= M; j++) {
            dis[i][j] = -1;
        }
    }

    init();
    queue<pair<int, int>> q;

    q.push({horizontal, vertical});
    dis[horizontal][vertical] = 0;
    
    while (!q.empty()) {
        auto [h, v] = q.front();
        q.pop();

        if (h == 0 && v == 0) {
            cout << dis[h][v] << endl;
            return 0;
        }

        for(auto& [nh, nv] : vector<pair<int, int>>{
            {h-1, M - v}, // 가로줄 하나 뒤집으면 세로는 전체 뒤집힘
            {h+1, M - v}, 
            {N - h, v-1}, // 세로줄 하나 뒤집으면 가로는 전체 뒤집힘
            {N - h, v+1}}) 
            {
            if (nh < 0 || nh > N || nv < 0 || nv > M) continue;
            if (dis[nh][nv] != -1) continue;

            dis[nh][nv] = dis[h][v] + 1;
            q.push({nh, nv});
        }
    }
    cout << -1 << endl; 

    return 0;
}