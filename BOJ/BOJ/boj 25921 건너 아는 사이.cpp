#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

using ll = long long;
/*
    모든 소수에 대하여, 배수들은 바로 연결됨 (비용 : 소수(공약수))
    모든 소수를 1과 연결 (비용 : 소수(큰수))
    그러면 최솟값이다.
*/
int main(){
    int N;
    cin >> N;

    ll ans = 0;

    vector<bool> isPrime(N + 1, true);
    isPrime[0] = isPrime[1] = false;

    // 2의 배수들을 모두 소수가 아니라고 표시
    for(int i = 4; i <= N; i += 2) {
        isPrime[i] = false;
        ans += 2; // 2와 연결하는 비용 추가
    }
    ans += 2; // 1과 연결하는 비용 추가

    // 3부터 N까지 모든 수에 대하여 소수 판별
    for(int i = 3; i <= N; i += 2) {
        if(isPrime[i]) {
            // i는 소수
            ans += i; // 1과 연결하는 비용 추가

        
            // i의 배수들을 모두 소수가 아니라고 표시
            for(int j = i + i; j <= N; j += i) {
                if(isPrime[j]) {
                    isPrime[j] = false;
                    ans += i; // i와 연결하는 비용 추가
                }
            }
        }
    }

    cout << ans << "\n";

    return 0;

}