#include <iostream>

using namespace std;

int N,K;
int table[1001][1001];
int MOD = 10007;
/*
   1
  1 1
 1 2 1


1
11
121
1331
14641
*/

int nCr(int n, int r) {
    if(n == r || r == 0) return 1;
    if(table[n][r] != 0) return table[n][r];
    return table[n][r] = (nCr(n-1,r-1)+ nCr(n-1,r))% MOD;
}

int main() {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    
    cin >> N >> K;

    cout << nCr(N,K) << endl;

}