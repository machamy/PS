#include <iostream> 
#include <vector>

using namespace std;

void solve(){
    int N;
    int res = 0;
    cin >> N;
    if(N == 1){
        cout << 1 << endl;
        return;
    }

    for(int i = 9; i > 1; i--){
        while(N && N % i == 0){
            res++;
            N /= i;
        }
    }
    // cout <<"tst " << N << " " << res << endl;
    if(N > 1){
        cout << -1 << endl;
        return;
    }

    cout << res << endl;
}


int main(){
    int T;
    cin >> T;
    while(T--){
        solve();
    }

    return 0;
}