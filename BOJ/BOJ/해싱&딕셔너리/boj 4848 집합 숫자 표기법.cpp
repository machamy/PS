#include <iostream>
#include <string>
#include <map>
using namespace std;

map<int, string> numToStr;
map<string, int> strToNum;


string get_str(int n) {
    if (n == 0) return "{}";
    string s = "{";
    for (int i = 0; i < n; i++) {
        s += numToStr[i];
        if (i != n - 1) s += ",";
    }
    s += "}";
    return s;
}

int main() {

    for (int i = 0; i <= 15; i++) {
        numToStr[i] = get_str(i);
        strToNum[numToStr[i]] = i;
    }

    int T;
    cin >> T;
    while (T--) {
        string a, b;
        cin >> a >> b;

        int x = strToNum[a];
        int y = strToNum[b];
        int res = x + y;

        cout << numToStr[res] << '\n';
    }

    return 0;
}
