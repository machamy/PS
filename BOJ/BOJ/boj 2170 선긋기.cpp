#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N;

struct line{
    int a, b;
};

struct cmp{
    bool operator()(const line &u, const line &v) const {
        if(u.a == v.a) {
            return u.b < v.b;
        }
        return u.a < v.a;
    };
};

vector<line> lines;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;

    for(int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        lines.push_back({a, b});
    }
    sort(lines.begin(), lines.end(), cmp());

    int s = lines[0].a;
    int e = lines[0].b;

    int ans = 0;
    for(int i = 1; i < N; i++) {
        if(lines[i].a <= e) {
            // 다음 선의 s 이전 선의가 e 보다 작거나 같으면 이어주기
            e = max(e, lines[i].b);
        } else {
            // 다음 선의 s 가 이전 선의 e 보다 크면 끊어진거니까 이전 선의 길이 더해주기
            ans += e - s;
            s = lines[i].a;
            e = lines[i].b;
        } 
    }
    ans += e - s;

    cout << ans << "\n";

    return 0;
}