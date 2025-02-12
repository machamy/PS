#include <iostream>
#include <vector>
#include <set>
using namespace std;



void solve() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    int largest = 0;
    cin >> n; // number of frogs
    int current_pos_arr[2 * 100000 + 1]; // i-th frog is at... by time
    for (int i = 0; i < n; ++i) {
        cin >> current_pos_arr[i];
        largest = max(largest, current_pos_arr[i]);
    }
    int q;
    cin >> q; // number of jumps
    vector<int> jumps(q); // i-th frog jumps... by time
    for (int i = 0; i < q; ++i) {
        cin >> jumps[i];
    }

    // 모든 빈공간을 찾아서 넣어준다.
    set<int> empty_set;
    for (int i = 1; i <= largest; ++i) {
        empty_set.insert(i);
    }

    for (int i = 0; i < n; ++i) {
        empty_set.erase(current_pos_arr[i]);
    }

        // cout << endl;
    for (int frog : jumps) {
        // empty에 있는 값중, frog의 현재 위치보다 큰 값중 가장 작은 값을 찾는다.
        // 그 값을 frog의 위치로 바꿔준다.
        auto it = empty_set.upper_bound(current_pos_arr[frog - 1]);
        // cout << "checking frog " << frog << " at " << current_pos_arr[frog - 1] << endl;
        int new_pos;
        // cout << "empty set: ";
        // for (int i : empty_set) {
        //     cout << i << " ";
        // }
        // cout << endl;
        if (it == empty_set.end()) {
            new_pos = largest + 1;
            largest++;
        }else{
            new_pos = *it;
            empty_set.erase(new_pos);
        }
        // cout << "new pos: " << new_pos << endl;
        empty_set.insert(current_pos_arr[frog - 1]);
        current_pos_arr[frog - 1] = new_pos;
        cout << new_pos << "\n";
    }
}

int main() {
    solve();
    return 0;
}
