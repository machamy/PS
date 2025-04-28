#include <iostream>
#include <cmath>
#include <list>
#include <algorithm>

using namespace std;


typedef long long ll;

ll A,B,K;
ll sum;

list<ll> factors;

int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    cin >> A >> B >> K;
    sum = A+B;
    // 최대 답은 A+B
    if(K >= A || K >= B)
    {
        cout << sum << endl;
        return 0;
    }

    if(B < A)
        swap(A,B);

    ll rt = ceil(sqrt(sum));
    for(int i = 1; i <= rt ; i++){
        if(sum % i == 0){
            factors.emplace_back(i);
        }
    }
    ll f_cnt = factors.size();
    for(auto i = factors.crbegin(); i != factors.crend();){
        ll f = *(i++);
        if(f*f != sum){
            factors.emplace_back((sum/f));
        }
    }

    // factors.push_back(sum);

    // B랑 A중 가능한 sum의 약수중에 가장 큰 값으로 만들면
    // 해당 약수가 정답

    for(auto i = factors.crbegin(); i != factors.crend();){
        ll f = *(i++);

        ll a = A % f;
        // cout << f << a << b << endl;
        if(a <= K || f - a <= K){
            cout << f << endl;
            return 0;
        }
    }
    cout << 1 << endl;
    return 0;
}