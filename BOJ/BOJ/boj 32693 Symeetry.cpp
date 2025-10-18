#include <iostream>
#include <vector>

using namespace std;



int N, M;
string S[501];
int dp[501][501];

/*
    dp[i][j] = i 행에서, j와 j+1 사이에 대칭이 되는 최대 길이

*/

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> N >> M;
    for(int i = 0; i < N; i++) cin >> S[i];

    for(int i = 0; i < N; i++){
        for(int j = 0; j < M - 1; j++){
            int l = j, r = j + 1;
            while(l >= 0 && r < M && S[i][l] == S[i][r]){
                dp[i][j] ++;
                l--;
                r++;
            }
        }
    }

    long long ans = 0;
    int L[501] = {0,}; // 왼쪽 최대 확장 가능한 길이, 같은 크기 포함 X
    int R[501] = {0,}; // 오른쪽 최대 확장 가능한 길이, 같은 크기 포함 O
    for(int col = 0; col < M - 1; col++){
        vector<int> st;
        for(int row = 0; row < N; row++){
            while(!st.empty() && dp[st.back()][col] >= dp[row][col]) st.pop_back();
            L[row] = st.empty() ? row + 1 : row - st.back();
            st.push_back(row);
        }
        st.clear();
        for(int row = N - 1; row >= 0; row--){
            while(!st.empty() && dp[st.back()][col] > dp[row][col]) st.pop_back();
            R[row] = st.empty() ? N - row : st.back() - row;
            st.push_back(row);
        }

        for(int row = 0; row < N; row++){
            ans += (long long)dp[row][col] * L[row] * R[row];
        }
    }
    cout << ans << endl;

}