#include <iostream>

using namespace std;
using ll = long long;
ll N,R;
/*
정수 N을 m으로 나눈 나머지가 R이 되도록 하는 모든 양의 정수 m의 합

16 을 예시로
0
0
1
0
1
4
2
0
7
...


1.
m은 적어도 R보다는 커야함.
2.
N//2 부터는 그냥 뺄셈임. 연산 필요 없음
3.
그러면 N//2보다 큰 값중에서 가능한걸 찾자
15 // 2 -> 7
14 = 15 - 1
13
12 
11
10
*/
int main(){
    cin >> N >> R;

    ll half = N/2;
    ll delta = N - R;
    if(R > half){
        if(N % delta == R){
            cout << delta << endl;
            return 0;
        } else{
            cout << 0 << endl;
            return 0;
        }
    }
    
    ll ans = 0;
    for(ll i = R+1; i <= N /2; i++){
        if(N % i == R){
            ans += i;
        }
        // cout << ans << endl;
    }
    if(N % delta == R){
        ans += delta;
    }
    cout << ans << endl;

    return 0;
}