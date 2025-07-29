#include <iostream>
#include <cmath>
#include <queue>
#include <vector>
using std::cin;
using std::cout;
using std::pair;
using std::priority_queue;
using std::max;

priority_queue<pair<long long, int>> pq;
long long ans;
int main()
{
    std::ios::sync_with_stdio(0);
    cin.tie(0);

    int N, D;
    cin >> N >> D;
    long long current; pair<long long, int> temp;
    cin >> current;
    ans = current; pq.push({current,0});
    for (long long i = 1;i < N;i++) {
        cin >> current;
        while (1) {
            if (i - pq.top().second > D) pq.pop();
            else break;
        }
        temp = pq.top(); pq.pop();
        pq.push({ max(temp.first + current, current),i });
        if (ans < pq.top().first) ans = pq.top().first;
        
        pq.push(temp);
    }
    cout << ans;

    return 0;
}