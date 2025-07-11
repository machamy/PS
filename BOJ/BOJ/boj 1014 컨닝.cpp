#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>


using namespace std;

int N, M;
char map[11][11];
int dp_table[10][1<<10];
vector<int> possibles[10];
void print_possibles(){
    // for(int i = 0; i < N; i++){
    //     cout << "row " << i << ": ";
    //     for(int j = 0; j < possibles[i].size(); j++){
    //         cout << possibles[i][j] << " ";
    //     }
    //     cout << "\n";
    // }
}

int dp(int row, int prev_bit){
    if(row == N){
        return 0;
    }
    if(dp_table[row][prev_bit] != -1){
        return dp_table[row][prev_bit];
    }

    int res = 0;
    for(int i = 0; i < possibles[row].size(); i++){
        int cur_bit = possibles[row][i];
        bool flag = true;
        int cnt = 0;
        for(int b = 0; b < M; b++){
            if(cur_bit & (1 << b)){
                // 현재 비트가 1인 경우
                cnt++;
                // if(prev_bit & (1 << b)){
                //     flag = false;
                //     break;
                // }
                if(prev_bit & (1 << (b + 1))){
                    flag = false;
                    break;
                }
                if(prev_bit & (1 << (b - 1))){
                    flag = false;
                    break;
                }
            }
        }
        if(flag){
            res = max(res, dp(row + 1, cur_bit) + cnt); 
        }
    }
    // cout << "row: " << row << ", prev_bit: " << prev_bit << ", res: " << res << "\n";
    dp_table[row][prev_bit] = res;
    return res;
}


void find_case(int row, int col, int bit){
    if(col >= M){
        possibles[row].push_back(bit);
        // cout << "row: " << row << ", bit: " << bit << "\n";
        return;
    }
    if(map[row][col] != 'x'){
        find_case(row,col + 2, bit | (1 << col));
    }
    find_case(row,col + 1, bit);
}

void solve()
{	
    memset(dp_table, -1, sizeof(dp_table));
    for(int i = 0; i < 10; i++){
        possibles[i].clear();
    }
    int ans = 0;

    cin >> N >> M;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++)
        {
            cin >> map[i][j];
        }
        find_case(i,0,0);
    }
    
    
    cout << dp(0,0) << "\n";
}


int main()
{
    ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
		solve();

	return 0;
}