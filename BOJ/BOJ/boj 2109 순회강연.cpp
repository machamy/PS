#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

using pii = pair<int,int>;

int N;
pii datas[10001];

bool cmp(pii a,pii b){
    if(a.first < b.first){
        return true;
    }
    if(a.first == b.first){
        return b.second < a.second;
    }
    return false;
}

int main(){
    cin >> N;

    for(int i =0; i <N;i++){
        int a,b;
        cin >> a >> b;
        datas[i] = make_pair(b,a);
    }

    sort(datas,datas+N,cmp);

    // for(int i =0; i <N;i++){
    //     cout << datas[i].first << ", " << datas[i].second << endl;
    // }
    
    priority_queue<int> ok;
    int prev_day = datas[N-1].first;
    int ans = 0;
    for(int i = N - 1; i >= 0;i--){
        int p,d;
        p = datas[i].second;
        d = datas[i].first;
        int days = prev_day - d;
        while(days-- && !ok.empty()){
            int x = ok.top(); ok.pop();
            ans += x;
            // cout << days << " added "<< x <<endl;
        }
        ok.emplace(p);
        prev_day = d;
    }
    int days = prev_day;
    while(days-- && !ok.empty()){
        int x = ok.top(); ok.pop();
        ans += x;
        // cout << days << " added "<< x <<endl;
    }

    cout << ans << endl;
    return 0;
}