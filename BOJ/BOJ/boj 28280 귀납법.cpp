#include <iostream>
#include <queue>
// #include <unordered_set>
#define MAX 4'000'010

using namespace std;

bool visited[MAX];

void reset(){
    for(int i = 0; i < MAX; i++){
        visited[i] = false;
    }
}

int T, k;

int main(){

    cin >> T;
    for(int i = 0; i < T; i++){
        cin >> k;
        queue<pair<int,int>> q;
        q.push({1, 0});
        reset();
        visited[1] = true;
        while(!q.empty()){
            auto [cur, cnt] = q.front();
            q.pop();
            // cout << cur << " " << cnt << endl;
            if(cur == k){
                cout << cnt << "\n";
                break;
            }
            int nxt = cur * 2;
            if(nxt <= MAX && !visited[nxt]){
                q.push({nxt, cnt + 1});
                visited[nxt] = true;
            }
            nxt = cur - 1;
            if(nxt > 1 && !visited[nxt]){
                q.push({nxt, cnt + 1});
                visited[nxt] = true;
            }
        }
    }
    
}