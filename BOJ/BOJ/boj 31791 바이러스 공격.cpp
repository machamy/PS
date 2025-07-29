#include <iostream>
#include <queue>

using namespace std;

int N, M;
int Tg,Tb,X,B;
int d4[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // 상하좌우
char world[1000][1000];

struct node {
    int x, y, abs_time;

    node(int x, int y,int abs_time) : x(x), y(y), abs_time(abs_time) {}
};

void debug() {
    // cout << "Current World State:\n";
    // for(int i = 0; i < N; i++) {
    //     for(int j = 0; j < M; j++) {
    //         cout << world[i][j];
    //     }
    //     cout << "\n";
    // }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin >> N >> M;
    cin >> Tg >> Tb >> X >> B;


    queue<node> q;
    queue<node> building;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cin >> world[i][j];
            if(world[i][j] == '*'){
                q.emplace(i, j, 0); // 점령된 지역
            }
        }
    }

    while(!q.empty() || !building.empty()) {
        node current = {0, 0, 0};
        if(q.empty()){
            current = building.front();
            building.pop();
        }else if(building.empty()) {
            current = q.front();
            q.pop();
        }else{
            if(q.front().abs_time < building.front().abs_time) {
                current = q.front();
                q.pop();
            }else{
                current = building.front();
                building.pop();
            }
        }
        if(current.abs_time >= Tg) break;; // 시간 초과
        if(world[current.x][current.y] == 'B'){
            current.abs_time += 1;
            world[current.x][current.y] = '*'; // 함락됨
            q.push(current);
            continue;
        }

        for(auto [di,dj] : d4) {
            int ni, nj;
            ni = current.x + di;
            nj = current.y + dj;

            if(ni < 0 || ni >= N || nj < 0 || nj >= M) continue;
            if(world[ni][nj] == '*' || world[ni][nj] == 'B') continue; // 이미 감염됨

            if(world[ni][nj] == '#'){
                world[ni][nj] = 'B';
                building.push({ni, nj, current.abs_time + Tb});
            }else{
                world[ni][nj] = '*'; // 점령됨
                q.push({ni, nj, current.abs_time + 1});
            }

            
        }
    }
    

    bool flag = false;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(world[i][j] != '*') {
                cout << i+1 << " " << j+1 << "\n";
                flag = true;
            }
        }
    }
    if(flag == false) {
        cout << "-1\n";
    }

    return 0;
}