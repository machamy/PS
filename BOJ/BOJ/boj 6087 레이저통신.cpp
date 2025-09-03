#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

const int MAX = 100;
const int INF = 1e9;

struct Entry {
    int x, y, dir;
};

int W, H;
char board[MAX][MAX];
int dist[MAX][MAX][4]; // x, y, direction

int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

bool isValid(int x, int y) {
    return (x >= 0 && x < W && y >= 0 && y < H && board[y][x] != '*');
}

int main() {
    cin >> W >> H;
    pair<int, int> start, end;

    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> board[i][j];
            if (board[i][j] == 'C') {
                if (!start.first && !start.second) start = { j, i };
                else end = { j, i };
            }
        }
    }

    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            for (int d = 0; d < 4; d++) {
                dist[i][j][d] = INF;
            }
        }
    }

    queue<Entry> q;
    for (int d = 0; d < 4; d++) {
        dist[start.second][start.first][d] = 0;
        q.push({ start.first, start.second, d });
    }

    int ans = INF;

    while (!q.empty()) {
        Entry current = q.front();
        q.pop();

        int x = current.x;
        int y = current.y;
        int dir = current.dir;
        if(current.x == end.first && current.y == end.second) {
            ans = min(ans, dist[y][x][dir]);
            continue;
        }

        for(int nxt_dir = 0; nxt_dir < 4; nxt_dir++) {
            int nxt_x = x + dx[nxt_dir];
            int nxt_y = y + dy[nxt_dir];
            int cost = dist[y][x][dir];
            if(!isValid(nxt_x, nxt_y)) continue;
            if(nxt_dir == dir){
                ;
            }else if(abs(nxt_dir - dir) == 2){
                continue;
            }else{
                cost++;
            }
            if(cost > ans) continue;
            if(cost < dist[nxt_y][nxt_x][nxt_dir]) {
                dist[nxt_y][nxt_x][nxt_dir] = cost;
                q.push({nxt_x, nxt_y, nxt_dir});
            }
        }
    }


    cout << ans << endl;

    return 0;
}