#include <iostream>

using namespace std;

int N,M;
int arr[301][301];
int dp[301][301];

// void printDP(){
//     for(int i = 0; i <= N; i ++){
//         for (int j = 0; j <= N; j++)
//         {
//             cout << dp[i][j] << " ";
//         }
//         cout << endl;
//     }
// }

int main(){
    cin >> N >> M;

    for(int i = 0; i < N; i++){
        int a,b;
        cin >> a >> b;
        arr[a][b] = M;
    }

    for(int j = 1; j <= 300; j++){
        dp[0][j] = dp[0][j-1] + max(0,arr[0][j] - j);
    }

    for(int i = 1; i <= 300; i++){
        dp[i][0] = dp[i-1][0] + max(0,arr[i][0] - i);
        for(int j = 1; j <= 300; j++){
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + max(0,arr[i][j] - i - j);
        }
        // printDP();
    }
    cout << dp[300][300] << endl;
    return 0;
}