#include <iostream>
#include <queue>
#include <utility>



using namespace std;

constexpr int SIZE = 4;
constexpr int TOTAL = SIZE * SIZE;
constexpr int MAX_STATE = 1 << TOTAL;

int original[SIZE][SIZE];
int target[SIZE][SIZE];

int KnightMoves[8][2] = {
    {2, 1}, {2, -1}, {-2, 1}, {-2, -1},
    {1, 2}, {1, -2}, {-1, 2}, {-1, -2}
};

bool isInBoard(int x, int y){
    return (x >= 0 && x < SIZE && y >= 0 && y < SIZE);
}

pair<int, int> getPos(int idx){
    return {idx / SIZE, idx % SIZE};
}

int dp[MAX_STATE];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    // state: 16비트
    // 0: 없음 1: 말
    int startState = 0;
    int targetState = 0;

    for(int i = 0; i < SIZE; i++){
            string input;
            cin >> input;
        for(int k = 0; k < SIZE; k++){
            original[i][k] = (input[k] == '1');
            startState = (startState << 1) | original[i][k];
        }
    }

    for(int i = 0; i < SIZE; i++){
        string input;
        cin >> input;
        for(int k = 0; k < SIZE; k++){
            target[i][k] = (input[k] == '1');
            targetState = (targetState << 1) | target[i][k];
        }
    }

    for(int i = 0; i < MAX_STATE; i++){
        dp[i] = -1;
    }

    queue<pair<int, int>> q;
    dp[startState] = 0;
    q.push({startState, 0});

    // cout << "Start State: " << startState << "\n";
    // cout << "Target State: " << targetState << "\n";

    while(!q.empty()){
        auto [currentState, currentDepth] = q.front();
        q.pop();

        if(currentState == targetState){
            cout << currentDepth << "\n";
            return 0;
        }

        for(int i = 0; i < TOTAL; i++){
            if(!(currentState & (1 << i))) continue;
            // i 위치에 말이 있음
            auto [x, y] = getPos(i);
            for(int d = 0; d < 8; d++){
                int nx = x + KnightMoves[d][0];
                int ny = y + KnightMoves[d][1];

                
                if(!isInBoard(nx, ny)) 
                    // 보드 밖
                    continue;
                int nIdx = nx * SIZE + ny;
                if(currentState & (1 << nIdx))
                    // 이미 말이 있음
                    continue;

                // 이동 가능
                int nextState = (currentState & ~(1 << i)) | (1 << nIdx);
                if(dp[nextState] != -1) continue;
                dp[nextState] = currentDepth + 1;
                q.push({nextState, currentDepth + 1});
            }
        }
    }
    // 이론상 불가능
    // assert(false);

    return 0;
}