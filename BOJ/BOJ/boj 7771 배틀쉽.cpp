#include <iostream>

using namespace std;

constexpr int SIZE = 10;

int D4i[8] = {1, -1, 0, 0, 1, 1, -1, -1};
int D4j[8] = {0, 0, 1, -1, 1, -1, 1, -1};


char board[SIZE][SIZE];
int shoots[100];

// tuple<int, int> getPos(int shoot){
//     int x = shoot / SIZE;
//     int y = shoot % SIZE;

//     return {x, y};
// }

void printBoard(){
    for(int i = 0; i < SIZE; i++){
        for(int j = 0; j < SIZE; j++){
            if(board[i][j] == 0) cout << ".";
            else cout << board[i][j];
        }
        cout << "\n";
    }
}

void markAdjacent(int x, int y){
    for(int d = 0; d < 8; d++){
        int nx = x + D4i[d];
        int ny = y + D4j[d];

        if(nx < 0 || nx >= SIZE || ny < 0 || ny >= SIZE) continue;
        if(board[nx][ny] == '#') continue;
        board[nx][ny] = '.';
    }
}

bool placeShip(int x, int y, int size, bool horizontal){
    if(horizontal){
        for(int i = 0; i < size; i++){
            if(board[x][y + i] != 0) return false;
        }
        for(int i = 0; i < size; i++){
            board[x][y + i] = '#';
            markAdjacent(x, y + i);
        }
    } else {
        for(int i = 0; i < size; i++){
            if(board[x + i][y] != 0) return false;
        }
        for(int i = 0; i < size; i++){
            board[x + i][y] = '#';
            markAdjacent(x + i, y);
        }
    }
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int lastX, lastY;

    for(int i = 0; i < 100; i++){
        cin >> shoots[i];
        if(shoots[i] == 100){
            lastX = i / SIZE;
            lastY = i % SIZE;
        }
    }
    // 걍 마지막 숫자에 # 두면 되는거 아님?

    /*
        전함의 수
    크기 1 : 4개
    크기 2 : 3개
    크기 3 : 2개
    크기 4 : 1개

        1. 마지막 숫자에 # 두기
        2. 다른 칸들에 전함 분배
        3. 이때 서로 인접하지 않도록
    */
    board[lastX][lastY] = '#';
    markAdjacent(lastX, lastY);

    // 전함 크기별로 배치
    int toPlace[4] = {3,3,2,1}; // 크기 1,2,3,4
    for(int size = 4; size >= 1; size--){
        while(toPlace[size - 1] > 0){
            bool placed = false;
            for(int i = 0; i < SIZE && !placed; i++){
                for(int j = 0; j < SIZE && !placed; j++){
                    if(board[i][j] != 0) continue;
                    // 가로
                    if(j + size <= SIZE && placeShip(i, j, size, true)){
                        toPlace[size - 1]--;
                        placed = true;
                        break;
                    }
                    // 세로
                    if(i + size <= SIZE && placeShip(i, j, size, false)){
                        toPlace[size - 1]--;
                        placed = true;
                        break;
                    }
                }
            }
        }
    }

    printBoard();
    return 0;
}