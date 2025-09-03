#include <iostream>
#include <vector>
#include <algorithm>

#define MAX_X 100001

using namespace std;

using pii = pair<int,int>;
vector<int> cafe_positions[MAX_X];

void clear_cafe_positions() {
    for (int i = 0; i < MAX_X; i++) {
        cafe_positions[i].clear();
    }
}

void solve(){
    vector<pii> cafe_list;

    clear_cafe_positions();

    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        int x, y;
        cin >> x >> y;
        cafe_positions[x].push_back(y); 
    }

    cafe_list.push_back({0,0});

    for(int x = 0; x < MAX_X; x++){
        vector<int>& current_vec = cafe_positions[x];
        if(current_vec.empty()) continue;

        sort(current_vec.begin(), current_vec.end());
        
        if(current_vec[0] != cafe_list.back().second){
            for(int i = current_vec.size() - 1; i >= 0; i--){
                cafe_list.push_back({x, current_vec[i]});
            }
        }else{
            for(int i = 0; i < current_vec.size(); i++){
                cafe_list.push_back({x, current_vec[i]});
            }
        }
    }

    int m;
    cin >> m;

    for(int i = 0; i < m; i++){
        int q;
        cin >> q;
        cout << cafe_list[q].first << " " << cafe_list[q].second << endl;
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int T;
    cin >> T;
    while(T--){
        solve();
    }

    return 0;
}