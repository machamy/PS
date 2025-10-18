#include <iostream>
#include <queue>

using namespace std;

using pii = pair<int, int>;
using ll = long long;

/*
0
1
2

가장 큰거 잘라서 1개씩 늘리는게 가능하다면 -> 그 방법으로
안되는 경우 작은것들을 모두 잘라야함
*/

ll N;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    if(N == 1){
        cout << "0\n";
        return 0;
    }

    ll tmp = 1;

    while((tmp * 2) < N){
        tmp <<= 1;
    }
    tmp--;
    // tmp 는 2^k - 1 꼴
    // 2^k개의 조각을 만드는데 필요한 자르기 횟수
    cout << tmp + (N + 1) / 2 << "\n";

    return 0;
}