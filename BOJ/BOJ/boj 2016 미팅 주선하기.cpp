#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cassert>

using namespace std;
using pii = pair<int, int>;

int boy2girl[5][5]; // [a][b] = c; a번 남학생이 b번 여학생을 c번째로 선호함.
int girl2boy[5][5]; // [a][b] = c; a번 여학생이 c번 남학생을 b번째로 선호함.
int pairings[5]; // 남학생 1~5의 현재 짝
int idxs[5]; // 여학생 6~10의 현재 인덱스



int cycle(){
    for(int i = 0; i < 5; i++){
        pairings[i] = -1;
        idxs[i] = 0;
    }

    queue<int> girlQue;
    for(int i = 0; i < 5; i++){
        girlQue.push(i);
    }

    while(!girlQue.empty()){
        int girl = girlQue.front();
        girlQue.pop();
        int boy = girl2boy[girl][idxs[girl]++];
        if(pairings[boy] == -1){
            pairings[boy] = girl;
        }else{
            if(boy2girl[boy][girl] < boy2girl[boy][pairings[boy]]){
                girlQue.push(pairings[boy]);
                pairings[boy] = girl;
            }else{
                girlQue.push(girl);
            }
        }
    }

    return pairings[0];
}

bool solve(){
    // 초기화
    for(int i = 0; i < 5; i++) {
        boy2girl[0][i] = i;
    }
    for(int i = 1; i < 5; i++){
        for(int rank = 0; rank < 5; rank++){
            int n;
            cin >> n;
            boy2girl[i][n-6] = rank;
        }
    }

    for(int i = 0; i < 5; i++){
        for(int rank = 0; rank < 5; rank++){
            int n;
            cin >> n;
            girl2boy[i][rank] = n-1;
        }
    }
    int origin = cycle();
    // cout << "origin: " << origin << "\n";
    for (int i = 1; i < 120; i++) {
        next_permutation(boy2girl[0], boy2girl[0] + 5);
        int current = cycle();
        if(current < origin){
            return true;
        }
    }
    return false;
}



int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int T;
    cin >> T;


    while (T--) {
        if(solve()){
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}