#include <iostream>
#include <queue>
using namespace std;

priority_queue <int, vector<int>, greater<int>> q;

int main()
{
    int n, num;
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> num;
        if (num != 0)
        {
            q.push(num);
        }
        else
        {
            if (q.empty())
            {
                cout << 0 << endl;
            }
            else
            {
                cout << q.top() << endl;
                q.pop();
            }
        }
    }
}