#include <iostream>
#include <vector>

using namespace std;

int N;
int arr[20001];
vector<int> factors;
bool visited[20001] = {false,};


int chk(int start_idx, int current_idx, int depth){
    visited[current_idx] = true;
    int nxt_idx = arr[current_idx];
    if(nxt_idx == start_idx){
        return depth;
    }
    return chk(start_idx, nxt_idx, depth + 1);
}

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int lcm(int a, int b) {
    return a / gcd(a, b) * b;
}

int lcm(vector<int> &v) {
    int ans = v[0];
    for (int i = 1; i < v.size(); i++) {
        ans = lcm(ans, v[i]);
    }
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    for(int i = 1; i <= N; i++){
        cin >> arr[i];
    }

    for(int i = 1; i <= N; i++){
        if(!visited[i]){
            int cnt = chk(i, i, 1);
            factors.push_back(cnt);
        }
    }

    int ans = lcm(factors);

    cout << ans << "\n";
    return 0;
}