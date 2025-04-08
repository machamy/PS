#include <iostream>
#include <queue>

using namespace std;

char world[1001][1001];

int D4i[4] = {-1,1,0,0};
int D4j[4] = {0,0,-1,1};

int solve();

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int i = 0; i < T; i++){
        int res =  solve();
        if(res >= 0){
            cout << res << "\n";
        }
        else{
            cout << "IMPOSSIBLE" << "\n";
        }
    }

    return 0;
}

int solve(){
    int w,h;
    cin >> w >> h;
    queue<pair<int,int>> fires;
    queue<pair<int,int>> player;
    
    for(int i = 0; i < h; i++){
        for(int j= 0; j< w; j++){
            cin >> world[i][j];
            if(world[i][j] == '*')
                fires.emplace(i,j);
            else if(world[i][j] == '@')
                player.emplace(i,j);
        }
    }

    int turn = 0;
    while(true){
        turn++;
        int playerQueueSize = player.size();
        // cout << turn << endl;
        for(int pqi = 0; pqi < playerQueueSize; pqi++){
            auto [previ, prevj] = player.front();
            player.pop();
            for(int dir = 0; dir < 4; dir++){
                
                if(world[previ][prevj] == '*'){
                    continue;
                }
                int ni = previ + D4i[dir];
                int nj = prevj + D4j[dir];
                // cout << ni << ' ' << nj << endl;
                if(ni < 0 || ni >= h || nj <0 || nj >= w){
                    return turn;
                }
                if(world[ni][nj] == '.'){
                    world[ni][nj] = '@';
                    player.emplace(ni,nj);
                    // cout << "emplace" << ni << nj << endl;
                }
            }
        }
        int fireQueueSize = fires.size();
        for(int fireIdx = 0; fireIdx < fireQueueSize; fireIdx++){
            auto [previ, prevj] = fires.front();
            fires.pop();
            for(int dir = 0; dir < 4; dir++){ 
                int ni = previ + D4i[dir];
                int nj = prevj + D4j[dir];
                if(ni < 0 || ni >= h || nj <0 || nj >= w){
                    continue;
                }
                if(world[ni][nj] == '.' || world[ni][nj] == '@'){
                    world[ni][nj] = '*';
                    fires.emplace(ni,nj);
                }
            }
        }

        if(playerQueueSize == 0){
            return -1;
        }
    }
}
