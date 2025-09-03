#include <iostream>
#include <vector>

using namespace std;

int K;
int traversal[1 << 11];

vector<int> ans[11];

void go(int lv, int start, int end){
    if (start > end) return;
    int mid = (start + end) / 2;
    ans[lv].push_back(traversal[mid]);
    go(lv + 1, start, mid - 1);
    go(lv + 1, mid + 1, end);
}

int main() {
    cin >> K;

    for (int i = 0; i < (1 << K) - 1; i++) {
        cin >> traversal[i];
    }

    go(0,0, (1 << K) - 2);

    for (int i = 0; i < K; i++) {
        for (int j = 0; j < ans[i].size(); j++) {
            cout << ans[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}