#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
N,M 쌍 찾기

1. N,M은 GCD의 배수여야함
2. N,M은 LCM의 약수여야함

3. N,M의 최대공약수가 GCD여야하고
4. N,M의 최대공배수가 LCM이어야함

a,b 는 서로소
N = aGCD
M = bGCD
LCM = a * b * GCD
LCM / GCD = a * b

LCM / GCD를 구한 후 해당 값을 두개의 서로소로 나누어봄
*/

using pii = pair<int,int>;

int GCD, LCM;

int gcd(int a, int b){
    int r = a % b;
    if(r == 0){
        return b;
    }
    return gcd(b,r);
}

int main() {
    cin >> GCD >> LCM;

    int div = LCM / GCD;

    int min_ans = GCD+LCM;
    pii ans;
    for(int factor = 1; factor*factor <= div; factor++){
        if(div % factor){
            continue;
        }
        // 약수임!
        int a = factor; 
        int b = div / factor;
        int chk = gcd(a,b);
        if(chk == 1){
            // 서로소!
            if(a+b < min_ans){
                ans = pii(a*GCD,b*GCD);
            }
        }else{
            continue;
        }
    }   
    cout << ans.first << " " << ans.second << endl;
    return 0;
}