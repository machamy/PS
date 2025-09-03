#include <iostream>

using namespace std;


int N, D;

int target;
int bit_flags[11];
int row_flags[11];
int col_flags[11];
int table[11][11];

bool inline chk_row(int r){
    return row_flags[r] == target;
}

bool inline chk_col(int c){
    return col_flags[c] == target;
}

bool dfs(int r, int c){

    // 완전 끝
    if(r == N){
        // 오른쪽 끝 열 확인.
        return chk_col(N - 1);
    }

    // 한 열의 끝행
    if(r == N - 1 && c > 0){
        if(!chk_col(c - 1)){
            return false;
        }
    }

    // 한 행의 끝
    if(c == N){
        if(chk_row(r)){
            return dfs(r + 1, 0);
        }
        return false;
    }

    
    if(table[r][c] != -1){
        // 이미 채워져 있는 칸
        return dfs(r, c + 1);
    }

    for(int num = 0; num < D; num++){
        int row_flag_bkup = row_flags[r];
        int col_flag_bkup = col_flags[c];
        table[r][c] = num;
        row_flags[r] |= bit_flags[num];
        col_flags[c] |= bit_flags[num];
        if(dfs(r, c + 1)){
            return true;
        }
        
        row_flags[r] = row_flag_bkup;
        col_flags[c] = col_flag_bkup;
        table[r][c] = -1;
    }

    return false;
}


int main(){
    cin >> N >> D;
    
    target = (1<<D) -1;

    for(int i = 0; i < 10; i++){
        bit_flags[i] = (1 << i);
    }

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            table[i][j] = -1;
        }
    }

    // 초기 미리 계산
    // N - D + 1개 만큼은 0으로 채우기
    int fill_zero = N - D + 1;
    for(int i = 0; i < fill_zero; i++){
        for(int j = 0; j < fill_zero; j++){
            table[i][j] = 0;
            col_flags[j] |= bit_flags[0];
            row_flags[i] |= bit_flags[0];
        }
    }
    // 채워진 행,열의 나머지 부분은 123456...으로
    for(int i = 0; i < fill_zero; i++){
        int cnt = 1;
        for(int j = fill_zero; j < N; j++){
            table[i][j] = cnt++;
            col_flags[j] |= bit_flags[table[i][j]];
            row_flags[i] |= bit_flags[table[i][j]];
        }
    }
    for(int j = 0; j < fill_zero; j++){
        int cnt = 1;
        for(int i = fill_zero; i < N; i++){
            table[i][j] = cnt++;
            row_flags[i] |= bit_flags[table[i][j]];
            col_flags[j] |= bit_flags[table[i][j]];
        }
    }

    // for(int i = 0; i < N; i++){
    //     for(int j = 0; j < N; j++){
    //         cout << table[i][j] << " ";
    //     }
    //     cout << "\n";
    // }

    bool chk = dfs(0, 0);
    if(chk == false){
        cout << "ERR" << endl;
    }
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cout << table[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}