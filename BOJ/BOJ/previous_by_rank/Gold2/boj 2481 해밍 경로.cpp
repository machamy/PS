#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <bitset>
#include <string>

using namespace std;

int path[100001];
vector<int> graph_by_id[100001];
unordered_map<int, int> num_to_id;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, K;
    cin >> N >> K;
    

    for (int i = 1; i <= N; ++i) {
        string binary;
        cin >> binary;
        int n = stoi(binary, nullptr, 2);
        num_to_id[n] = i;
    }

    for(auto it = num_to_id.begin(); it != num_to_id.end(); ++it) {
        int n, id;
        n = it->first;
        id = it->second;
        for (int j = 0; j < K; ++j) {
            int bit = 1 << j;
            int nxt = n ^ bit;
            if (num_to_id.find(nxt) != num_to_id.end()) {
                int nxt_id = num_to_id[nxt];
                graph_by_id[id].push_back(nxt_id);
            }
        }
    }

    queue<int> q;
    q.push(1);

    while (!q.empty()) {
        int id = q.front();
        q.pop();
        for (int nxt_id : graph_by_id[id]) {
            if (path[nxt_id] == 0) {
                path[nxt_id] = id;
                q.push(nxt_id);
            }
        }
    }

    int M;
    cin >> M;
    for (int i = 0; i < M; ++i) {
        int id;
        cin >> id;
        if (path[id] == 0) {
            cout << -1 << '\n';
            continue;
        }
        vector<int> ans;
        while (id != 1) {
            ans.push_back(id);
            id = path[id];
        }
        ans.push_back(1);
        for (auto it = ans.rbegin(); it != ans.rend(); ++it) {
            cout << *it << ' ';
        }
        cout << '\n';
    }

    return 0;
}