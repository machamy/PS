#include <iostream>
#include <algorithm>
#include <vector>

#ifndef ONLINE_JUDGE
#define dbg(x) cout << #x << " = " << (x) << endl;
#else
#define dbg(x) ;
#endif

using namespace std;
using pii = pair<int, int>;

int N, M;
int ans = 0;
pii Data[200'001];
vector<pii> queue; // {value, remaining}

int cmp(const pii &a, const pii &b) {
    // first 값이 더 크면 앞으로
    if (a.first > b.first) return true;
    if (a.first == b.first) {
        return a.second > b.second;
    }
    return false;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    for (int i = 1; i <= M; i++) {
        cin >> Data[i].first;
        ans += Data[i].first;
    }
    for (int i = 1; i <= M; i++) {
        cin >> Data[i].second;
    }

    for (int i = 1; i <= M; i++) {
        auto [baseScore, upScore] = Data[i];
        int count = (100 - baseScore) / upScore;
        int remaining = (100 - baseScore) % upScore;
        if (count > 0) {
            queue.push_back({upScore, count});
        }
        if (remaining > 0) {
            queue.push_back({remaining, 1});
        }
    }

    sort(queue.begin(), queue.end(), cmp);


    int time = 24 * N;
    
    int idx = 0;
    while(time > 0 && idx < queue.size()) {
        auto [score, count] = queue[idx];
        if (time < count){
            ans += time * score;
            time = 0;
            break;
        }
        else{
            ans += count * score;
            time -= count;
        }
        dbg(time);
        dbg(ans);
        idx++;
    }

    cout << ans << '\n';

    return 0;
}