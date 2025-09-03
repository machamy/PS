#include <iostream>
#include <vector>
#include <algorithm>

#define FASTIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

#define MAX 100000


using namespace std;

using ll = long long;
using pii = pair<int, int>;




int N;

vector<int> points[MAX+1];
int closest[MAX+1];

int bisect(int pos, int color){
    int left = 0;
    int right = points[color].size() - 1;
    int mid;
    while(left <= right){
        mid = (left + right) / 2;
        if(points[color][mid] == pos){
            return mid;
        }else if(points[color][mid] < pos){
            left = mid + 1;
        }else{
            right = mid - 1;
        }
    }
    return left;
}

int get_closest(int pos,int color){
    int min_dist = MAX + 100;
    int res = -1;
    if(closest[pos] != -1){
        return closest[pos];
    }
    int idx = bisect(pos, color);
    // cout << "Checking position " << pos << " in color " << color << ": ";
    // cout << "idx = " << idx << "\n";
    for(int delta = 1; idx + delta < points[color].size() || idx - delta >= 0; delta++){
        if(idx + delta < points[color].size()){
            int dist = abs(pos - points[color][idx+delta]);
            if(min_dist > dist){
                min_dist = dist;
                res = points[color][idx+delta];
            }
        }
        if(idx - delta >= 0){
            int dist = abs(pos - points[color][idx-delta]);
            if(min_dist > dist){
                min_dist = dist;
                res = points[color][idx-delta];
            }
        }
    }
    closest[pos] = res;
    return res;
}

int main(){
    FASTIO;
    cin >> N;

    for(int i = 0; i < N; i++){
        int x, y;
        cin >> x >> y;
        points[y].push_back(x);
    }
    
    for(int i = 0; i <= N; i++){
        sort(points[i].begin(), points[i].end());
    }

    for(int i = 0; i <= MAX; i++){
        closest[i] = -1;
    }

    int ans = 0;
    for(int i = 0; i <= MAX; i++){
        if(points[i].empty()) continue;
        for(int p: points[i]){
            int c = get_closest(p, i);
            ans += abs(p - c);
            if(c == -1){
                cout << p << "\n";
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
