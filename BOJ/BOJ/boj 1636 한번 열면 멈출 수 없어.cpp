#include <iostream>
#include <vector>

using namespace std;

using pii = pair<int, int>;

int N;
pii arr[100'001];


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> arr[i].first >> arr[i].second;
    }

    // 가능한 범위의 숫자
    vector<pii> res;

    // 초기값 구하기
    if(arr[0].second < arr[1].first){
        // 서로 안겹침. 앞에있음
        res.push_back({arr[0].second, arr[0].second});
    }
    else if (arr[0].first > arr[1].second){
        // 서로 안겹침. 뒤에있음
        res.push_back({arr[0].first, arr[0].first});
    }
    else {
        // 겹치는 경우.
        res.push_back({max(arr[0].first, arr[1].first), min(arr[0].second, arr[1].second)});
    }
    pii current = res[0];

    for(int i = 1; i < N; i++){
        if(current.second < arr[i].first){
            current.first = current.second = arr[i].first;
        }
        else if(current.first > arr[i].second){
            current.first = current.second = arr[i].second;
        }
        else {
            // 겹치는 경우. 교집합 구하기
            current.first = max(current.first, arr[i].first);
            current.second = min(current.second, arr[i].second);
        }
        res.push_back(current);
    }

    

    // for(auto [l, r] : res){
    //     cout << l << ' ' << r << '\n';
    // }

    vector<int> ans;
    ans.push_back(res[N-1].second);
    int cursor = ans.back();

    for(int i = N-2; i >= 0; i--){
        int& L = res[i].first;
        int& R = res[i].second;
        if(cursor < L){
            cursor = L;
        }else if(cursor > R){
            cursor = R;
        }
        ans.push_back(cursor);
    }
    int sum = 0;
    for(int i = 1; i < ans.size(); i++){
        sum += abs(ans[i] - ans[i-1]);
    }
    cout << sum << "\n";
    for(int i = ans.size()-1; i >=0 ; i--){
        cout << ans[i] << "\n";
    }

    return 0;
}