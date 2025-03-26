#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int H,W;

int A[10][10];
int B[10][10];
int dp[11][11]; // i행에서

int cal(int a,int b){
    int tmp = (a-b);
    return tmp * tmp;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> H >> W;

    for(int i = 0; i < H; i++){
        for(int j = 0; j < W; j++){
            cin >> A[i][j];
        }
    }

    for(int i = 0; i < H; i++){
        for(int j = 0; j < W; j++){
            cin >> B[i][j];
        }
    }

    for(int i = 0; i < H; i++){
        for(int j = 0; j < W; j++){
            dp[i+1][j] = cal(A[i][j],B[i][j]);
            int low = dp[i][j];
            if(j > 0)
                low = min(low,dp[i][j-1]);
            if(j < W -1)
                low = min(low,dp[i][j+1]);
            dp[i+1][j] += low;
        }
    }


    // for(int i = 0; i <= H; i++){
    //     for(int j = 0; j < W; j++){
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    cout << *min_element(dp[H],dp[H] + W) << endl;
}