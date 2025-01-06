#include <iostream>
#include <vector>

using namespace std;

void fastio() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}


int N, S, E;

vector<int> tree[100'001];
int prev_node[100'001] = { 0, };

vector<int> findPath() {
    vector<int> result;
    int current = E;
    while (current != S) {
        result.push_back(current);
        current = prev_node[current];
    }
    return result;
}

bool dfs(int node) {
    if (node == E) {
        return true;
    }
    for (int nxt : tree[node]) {
        if (prev_node[nxt] != 0)
            continue;
        prev_node[nxt] = node;
        if (dfs(nxt))
            return true;
    }
    return false;
}

int main() {
    fastio();
    cin >> N >> S >> E;
    for (size_t i = 0; i < N - 1; i++)
    {
        int a, b;
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    prev_node[S] = -1;
    dfs(S);
    vector<int> reversed_path = findPath();
    for (int i = reversed_path.size() - 1; i > 0; i -= 2) {
        int n = reversed_path[i];
        if (tree[n].size() - 1 > 1) {
            cout << "Second" << "\n";
            return 0;
        }
    }
    cout << "First" << "\n";

    return 0;
}