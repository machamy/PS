#include <iostream>

using namespace std;

int W,N;
int arr[5001];
int dp[800'000];


int main(void){
    int current;
    cin >> W >> N;

    for(int i = 0; i < N; i++){
        cin >> arr[i];
    }
    // A+B+C+D = W 
    // A+B = W - (C+D)
    for (int i = 0; i < N; i++)
    {
        // A+B = W - (C+D) 확인과정
        for (int j = i+1; j < N; j++)
        {
            if(arr[i]+arr[j]>W) continue;
            if(dp[W-arr[i]-arr[j]]){
                cout << "YES\n";
                return 0;
            }
        }

        // A+B 저장과정
        for (int k = 0; k < i; k++){
            if(arr[i]+arr[k] < W){
                dp[arr[i]+arr[k]]=1;
            }
        }
    }
    
    cout << "NO\n";

    return 0;
}