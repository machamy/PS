#include <iostream>
#include <cmath>
#include <queue>
#include <vector>

using namespace std;

typedef long long ll;

int N, D;

priority_queue<pair<ll, int>> pq;
ll ans;
int main()
{
    std::ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> D;
    ll current; 
    

    // 첫 값은 그냥 넣기
    cin >> current;
    ans = current;
    pq.emplace(current, 0);
    for (ll i = 1;i < N;i++) {
        cin >> current;
        // D 보다 멀리있는 기존 값은 없애기
        while (true) {
            if (i - pq.top().second > D)
                pq.pop();
            else
                break;
        }
        // D 거리 이내의 최대값 가져오기
        pair<ll, int> temp = pq.top();

        // 현재값을 포함하는 경우
        pq.emplace(max(temp.first + current, current), i);
        if (ans < pq.top().first)
            ans = pq.top().first;
    }
    cout << ans;

    return 0;
}