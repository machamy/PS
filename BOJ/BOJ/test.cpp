
#include <bits/stdc++.h>

using namespace std;
using ll = long long;

int reading_bit[7] {1, 2, 4, 8, 16, 32, 64};

int main()
{
    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        if (n == 1)
        {
            cout << "1\n1\n";
            continue;
        }

        if (n == 2)
        {
            cout << "2\n1 2\n";
            continue;
        }

        int l = 0, r = 6;
        int bit_reader;

        while (l <= r)
        {
            int m = (l + r) / 2;
            if (reading_bit[m] <= n)
            {
                bit_reader = m;
                l = m + 1;
            }
            else
            {
                r = m - 1;
            }
        }

        int dont_access = reading_bit[bit_reader] | reading_bit[bit_reader - 1];

        vector<int> res;
        for (int i = reading_bit[bit_reader - 1]; i < min(n + 1, dont_access); ++i)
            res.push_back(i);
        cout << res.size() << '\n';
        for (int &i: res)
            cout << i << ' ';
        cout << '\n';
    }
}