#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int N;

int solve();
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cout << "Case #"<< i+1  <<": "<< solve()<< endl;
    }   
}
int S,Q;
string searchEngines[200];
string queries[1000];

int dp[1001][201];
int solve(){
    cin >> S;
    cin.ignore();
    for (int i = 0; i < S; i++)
    {
        getline(cin,searchEngines[i]);
    }
    cin >> Q;
    cin.ignore();
    for (int i = 0; i < Q; i++)
    {
        getline(cin,queries[i]);
    }
    // cout << endl << N << S << Q <<endl;

    /*
    if nxtEngine != q
        dp[i][nxtEngine] = dp[i-1][engine] 
    if nxtEngine == q
        dp[i][nxtEngine] = dp[i-1][engine] 
    */
//    cout << endl;
    for (int i = 1; i <= Q; i++)
    {
        string q = queries[i-1];
        // cout << "q : " << i << " "<< q << endl;
        int minimumIdx = min_element(dp[i-1],dp[i-1] + S) - dp[i-1];
        for(int nxtEngine = 0; nxtEngine < S; nxtEngine++){
            if(searchEngines[nxtEngine] == q)
                {
                    dp[i][nxtEngine] = 2000;
                    continue;
                }
            dp[i][nxtEngine] = min(dp[i-1][minimumIdx] + 1, dp[i-1][nxtEngine]);
            // cout << "dp[" <<i << "]["<<nxtEngine<<"] : " <<  dp[i][nxtEngine] << endl;
            
        }
        
    }

    // for (size_t j = 0; j < S; j++)
    //     {
    //         cout << dp[Q][j] << endl;
    //     }
    // cout <<min_element(dp[Q],dp[Q] + (S)) - dp[Q] ;
    return *min_element(dp[Q],dp[Q] + S);
}