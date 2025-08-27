#include <iostream>

using namespace std;

int dp[1001];
int price[1001];


int main(){
    int N;
    cin >> N;
    price[0] = 0; 
    for(int i = 1; i <= N; i++){
        cin >> price[i];
    }

    for(int i = 0; i <= N; i++){
        dp[i] = -1;
    }

    dp[0] = 0;
    dp[1] = price[1];
    for(int i = 2; i <= N; i++){
        dp[i] = price[i];
        for(int j = 1; j <= i; j++){
            dp[i] = min(dp[i], dp[i-j] + price[j]);
        }
    }
    cout << dp[N] << endl;
}