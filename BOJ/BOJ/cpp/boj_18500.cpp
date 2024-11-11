#include <iostream>
#include <queue>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int R, C;
int d4r[4] = {1, -1, 0, 0};
int d4c[4] = {0, 0, 1, -1};
char arr[100][100] = {
    0,
};

int dfs()
{
}

int doit(int i, int j)
{
    int cnt = 1;
    int visited[100][100] = {
        0,
    };

    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if (arr[i][j] == 'x' && visited[i][j] == 0)
            {
                bool ok = false;
                queue<pair<int, int>> q;

                while (!q.empty)
                {
                    int r = q.front().first;
                    int c = q.front().second;
                    q.pop();
                    for (int idx = 0; k < 4; k++)
                    {
                        int n_r, n_c;
                        n_r = r+d4r[k];
                        n_
                    }
                }
            }
        }
    }
}

int main(void)
{
    cin >> R >> C;

    for (int i = 0; i < R; i++)
    {
        string str;
        cin >> str;
        for (int j = 0; j < C; j++)
        {
            arr[i][j] = str[j];
        }
    }

    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int h;
        cin >> h;
        if (i & 1)
        {
            for (int j = 0; j < C; j++)
            {
                if (arr[i][j] == 'x')
                {
                    doit(i, j);
                    break;
                }
            }
        }
        else
        {
            for (int j = C - 1; j >= 0; j--)
            {
                if (arr[i][j] == 'x')
                {
                    doit(i, j);
                    break;
                }
            }
        }
    }

    return 0;
}
