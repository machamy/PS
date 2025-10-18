#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;


using ll = long long;
using ull = unsigned long long;
/*
  1 3 15 63 255 1023
  1 11 1111 111111 11111111 1111111111
  의 배수 판정?

  
*/

unordered_map<ull,ull> mp{ {1, 1}, {3, 1}, {15, 1}, {63, 1}, {255, 1}, {1023, 1} };

ull P = 1e9 + 7;

ull C = 406367296; // (1 << 1023) % P

int main() {
    int N;
    cin >> N;
    ll X = 0;

    C = (1 << 1023) % P;

    int target = N / 1023 * 1023;
    int start = 1;
    auto it = mp.find(target);

    if(it != mp.end()){
        start = &it->second;
    }

    for(int i = start; i <= N; i++){

        {
            X = X - i;
            if(X < 0) X *= -1;
        }

        if(i % 3 == 0){
            ull temp = (ull)X * (ull)i;
            X = (ll)(temp % (ull)P);
        }

        if(i % 15 == 0){
            X &= i;
        }

        if(i % 63 == 0){
            X ^= i;
        }

        if(i % 255 == 0){
            X |= i;
        }

        // if(i % 1023 == 0){
        //     X <<= i;
        //     X %= P;
        // }
    }

    cout << X << endl;

    return 0;
}