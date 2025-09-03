#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;


int N, K;

// struct Trie {
//     struct Node {
//         char c;
//         Node* child[26];
//         Node(char ch = 0) : c(ch) {
//             for (auto &p : child) p = nullptr;
//         }
//     };
//     Node* root;
//     int node_count;
//     Trie() : root(new Node()), node_count(0) {}

//     static inline int idx(char ch) {
//         return ch - 'A';
//     }

//     int size() const { return node_count; }

//     void insert_prefix(const string& s, int n) {
//         Node* cur = root;
//         for (int i = 0; i < n; ++i) {
//             int k = idx(s[i]);
//             if (!cur->child[k]) { cur->child[k] = new Node(s[i]); ++node_count; }
//             cur = cur->child[k];
//         }
//     }

//     void insert_postfix(const string& s, int n) {
//         Node* cur = root;
//         int L = (int)s.size();
//         for (int i = L - 1; i >= L - n; --i) {
//             int k = idx(s[i]);
//             if (!cur->child[k]) { cur->child[k] = new Node(s[i]); ++node_count; }
//             cur = cur->child[k];
//         }
//     }
// };

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> K;
    // Trie prefix, postfix;
    unordered_set<ll> prefix, postfix;

    string s;

    for (int i = 0; i < N; ++i) {
        cin >> s;
        ll hash_pre = 0;
        ll hash_post = 0;
        for(int j = 0; j < K; ++j) {
            hash_pre = hash_pre * 31 + s[j];
            hash_post = hash_post * 31 + s[s.size() - 1 - j];
            prefix.insert(hash_pre);
            postfix.insert(hash_post);
        }
    }

    cout << prefix.size() + postfix.size() << "\n";
    // cout << prefix.size() << " " << postfix.size() << "\n";
    return 0;
}