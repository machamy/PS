#include <iostream>
#include <vector>
#include <algorithm>

#define FASTIO ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)

using namespace std;
vector<pair<int,int>> datas;
int start_idx = 0;
int N,K,S;

int go(bool is_left){
    int cnt;
    int remain = K;
    int pos = S;
    if(is_left){
        cnt = S - datas[start_idx].first;
        cnt *= 2;
        while(start_idx != datas.size()){
            if(datas[start_idx].second > remain){
                datas[start_idx].second -= remain;
                return cnt;
            }
            remain -= datas[start_idx].second;
            pos = datas[start_idx].first;
            start_idx++;
            if(datas[start_idx].first > S){
                break;
            }
        }
    }
    else{
        cnt = datas.back().first - S;
        cnt *= 2;
        while(!datas.empty()){

            if(datas.back().second > remain){
                
                datas.back().second -= remain;
                return cnt;
            }
            remain -= datas.back().second;
            pos = datas.back().first;
            datas.pop_back();
            if(datas.back().first < S){
                break;
            }
        }
    }
    return cnt;
}

int main(){
    FASTIO;

    cin >> N >> K >> S;

    for(int i = 0; i < N; i++){
        int a,b;
        cin >> a >> b;
        datas.push_back({a,b});
    }
    sort(datas.begin(),datas.end()
    ,[](pair<int,int> a, pair<int,int> b){
        if (a.first == b.first) 
            return a.second < b.second;
        return a.first < b.first;
    });
    int ans = 0;
    while(start_idx != datas.size()){
        
        // 양 끝단중 더 먼값
        bool is_left = false;
        int left = S - datas[start_idx].first;
        int right = datas.back().first - S;
        if(left < 0){
            // 왼쪽 전멸
            ans += go(false);
            // cout << is_left << "gg " << ans << endl;
            continue;    
        }

        if(right < 0){
            // 오른쪽 전멸
            ans += go(true);
            // cout << is_left << "gg " << ans << endl;
            continue;
        }

        if(left > right){
            is_left = true;
        }
        ans += go(is_left);

        // cout << is_left << " " << ans << endl;
    }
    cout << ans << endl;
    return 0;
}