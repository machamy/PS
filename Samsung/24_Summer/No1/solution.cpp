#define UP 0
#define RIGHT 1
#define DOWN 2
#define LEFT 3

#include <queue>
#include <vector>
#include <unordered_set>
#include <cstring>
#include <string>

using namespace std;

extern bool swap(int dir);


class Board{
    public:
    int board[5][5];
    vector<int> answer;
    int cnt;
    int emptyX,emptyY;

    Board(int board[5][5]){
        memcpy(this->board,board,sizeof(int) * 25);
        for(int i = 0; i < 5; i ++){
            for(int j = 0 ; j <5 ; j++){
                if(board[i][j] == 0){
                    emptyX = j;
                    emptyY = i;
                    goto end;
                }
            }
        }
        end:;
    }

    bool isOk(int pattern[3][3]){
        for(int i = 0; i < 3; i ++){
            for(int j = 0 ; j <3 ; j++){
                if(board[2+i][2+j] != pattern[i][j])
                    return false;
            }
        }
        return true;
    }

    bool swap(int dir){
        int dy[4] = { -1, 0, 1, 0 };
        int dx[4] = { 0, 1, 0, -1 };

        ++cnt;

        if (dir < UP || dir > LEFT) {
            return false;
        }

        int newY = emptyY + dy[dir];
        int newX = emptyX + dx[dir];

        if (newY < 0 || newY >= 5 || newX < 0 || newX >= 5) {
            return false;
        }

        board[emptyY][emptyX] = board[newY][newX];
        board[newY][newX] = 0;
        emptyY = newY;
        emptyX = newX;
        answer.push_back(dir);

        return true;
    }

    const bool operator==(const Board& a)const {
        for(int i = 0; i < 5; i ++){
            for(int j = 0 ; j <5 ; j++){
                if(board[i][j] != a.board[i][j]){
                    return false;
                }
            }
        }
        return true;
    }

    const bool operator<(const Board& a)const {
       return cnt < a.cnt;
    }
};

namespace std{
    template<>
    struct hash<Board>{
        size_t operator()(const Board& board) const{
            size_t result = 0;
            for(int i = 0; i < 5; i ++){
                for(int j = 0 ; j <5 ; j++){
                    result = result * 13 + board.board[i][j];
                }
            }
            for(int dir : board.answer){
                result = result * 13 + dir;
            }
            return result;
        }
    };
}


void solve(int board[5][5], int pattern[3][3], int callCntLimit) {
    priority_queue<Board> q;
    q.push(Board(board));
    vector<int> answer;
    unordered_set<Board> visited;

    while(!q.empty()){
        Board current = q.top();
        q.pop();
        visited.insert(current);

        if(current.isOk(pattern))
            {
                answer = current.answer;
                break;
            }
        
        for(int dir = 0; dir < 4; dir++){
            Board next = current;
            if(next.swap(dir)){
                if (visited.find(next) == visited.end() && next.cnt <= callCntLimit) {
                    q.push(next);
                }
            }
        }

    }

    for(int dir : answer){
        swap(dir);
    }
}