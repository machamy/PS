#include <bits/stdc++.h>
#define fi first
#define se second
#define all(a) (a).begin(), (a).end()

using namespace std;
using ll = long long;
using pii = pair<int, int>;

bool a[26];
char str[26];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    if (s == "zyxwvutsrqponmlkjihgfedcba") {
        cout << -1;
        return 0;
    }

    if (s.length() != 26) {
        for (char c : s) {
            a[c-'a'] = true;
        }
        for (int i = 0; i < 26; i++) {
            if (!a[i]) {
                cout << s << (char)(i+'a');
                return 0;
            }
        }
    }

    for (int i = 0; i < 26; i++) {
        str[i] = s[i];
    }
    next_permutation(str, str+27);
    cout << str << endl;
    for (int i = 0; i < 26; i++) {
        cout << i << str[i];
    }
}