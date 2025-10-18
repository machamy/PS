#include <iostream>
#include <queue>
#include <unordered_set>

using namespace std;

using ll = long long;


struct Node {
    ll val;
    int cnt;
};

unordered_set<ll> visited;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll N;
    cin >> N;

    queue<Node> q;
    q.push({N, 0});

    while(!q.empty()){
        Node curr = q.front();
        q.pop();
        auto[val, cnt] = curr;
        if(val == 1){
            cout << cnt << "\n";
            break;
        }

        auto append = [&](ll n){
            if(visited.find(n) == visited.end()){
                visited.insert(n);
                q.push({n, cnt + 1});
            }
        };

        if(val % 3 == 0){
            append(val / 3);
        }
        if(val % 2 == 0){
            append(val / 2);
        }

        append(val - 1);
        
        
    }

    return 0;
}