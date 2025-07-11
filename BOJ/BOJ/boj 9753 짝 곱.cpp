#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

#define MAX 200'000

using namespace std;
typedef long long ll;

int T;
int K;

bool primeTable[MAX + 1];
vector<int> primes;
set<int> muls;
int solve(){
    cin >> K;
    
    int k = K;
    
    ll ans = 999'999;
    for(int i = 0; i < primes.size(); i++){
        if(primes[i] > ans){
            break;
        }
        for(int j = i+1; j < primes.size(); j++){
            ll n = (ll)primes[i] * primes[j];
            // cout << ans << " "<<  n << ' ' << primes[i] << ' ' << primes[j] << '\n';
            if(n > ans){
                // cout << "break\n";
                break;
            }
            if(n>= K){
                ans = min(ans, n);
                continue;
            }
            
        }
    }

    return ans;
}

int main(){
   
    for(int i = 0; i <= MAX; i++){
        primeTable[i] = true;
    }

    primeTable[1] = primeTable[0] = false;
    int p;
    for(int i = 2; i <= MAX; i++){
        if(primeTable[i]){
            primes.push_back(i);
            for(int j = i * 2; j <= MAX; j += i){
                primeTable[j] = false;
            }
        }
    }
    // sort(primes.begin(), primes.end());
    // for(int i = 0; i < primes.size(); i++){
    //     cout << primes[i] << ' ';
    // }

    cin >> T;
    while(T--){
        cout << solve() << '\n';
    }

    return 0;

}