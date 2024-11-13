#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

int N, M, Fuel;
// int arr[20][400];
int map[21][21];

struct Passenger
{
    int i;
    int j;

    int ii;
    int jj;
};

Passenger pArr[401];
void main()
{
    cin >> N >> M >> Fuel;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> -map[i + 1][j + 1];
        }
    }
    int texyI, texyJ;
    cin >> texyI >> texyJ;

    for (int idx = 0; idx < M; idx++)
    {
        int i, j, ii, jj;
        cin >> i >> j >> ii >> jj;
        pArr[idx + 1].i = i;
        pArr[idx + 1].j = j;
        pArr[idx + 1].ii = ii;
        pArr[idx + 1].jj = jj;

        map[i][j] = idx + 1;
    }

    int pCounter = M;
    while (pCounter > 0)
    {
        vector<int> pVector;
        dfs_passenger(texyI, texyJ, pVector);
        if (pVector.empty())
        {
            cout << -1 << endl;
            return;
        }

        sort(pVector.begin(), pVector.end(), p_sort);
    }
}

struct dfsData
{
    int i;
    int j;
    int distance;
    int pCode;
};

int di[4] = {0, 0, -1, 1};
int dj[4] = {1, -1, 0, 0};

int p_sort(int a, int b)
{
    Passenger A = pArr[a], B = pArr[b];
    if (A.i < B.i)
        return true;
    if (A.i > B.i)
        return false;
    return A.j < B.j;
}

void dfs_passenger(int i, int j, vector<int> &result)
{
    queue<tuple<int, int, int>> q;
    q.push(make_tuple(start, end, Fuel, 0));
    int minDistance = 210000;
    while (!q.empty())
    {
        tuple<int, int, int> e = q.pop();
        int i, j, f, c;
        i = get<0>(e);
        j = get<1>(e);
        f = get<2>(e);
        c = get<3>(e);
        if (c > minDistance)
            continue;
        if (map[i][j] > 0)
        {
            result.push_back(map[i][j]);
            minDistance = c;
            continue;
        }
        if (f <= 0)
            continue;
        for (int d = 0; d < count; d++)
        {
            int ni, nj;
            ni = i + di[d];
            nj = j + dj[d];
            if (ni < 0 || ni >= N || nj < 0 || nj > N)
                continue;
            q.push(make_tuple(ni, nj, f - 1, c + 1));
        }
    }
}

void dfs_passenger(int pCode)
{
    queue<tuple<int, int, int>> q;
    q.push(make_tuple(pArr[pCode].i, pArr[pCode].j, Fuel, 0));
    while (!q.empty())
    {
        tuple<int, int, int> e = q.pop();
        int i, j, f, c;
        i = get<0>(e);
        j = get<1>(e);
        f = get<2>(e);
        c = get<3>(e);
        if (i == pArr[pCode].ii && j == pArr[pCode].jj)
        {
            return f;
        }
        if (f <= 0)
            continue;
        for (int d = 0; d < count; d++)
        {
            int ni, nj;
            ni = i + di[d];
            nj = j + dj[d];
            if (ni < 0 || ni >= N || nj < 0 || nj > N)
                continue;
            q.push(make_tuple(ni, nj, f - 1, c + 1));
        }
    }
    return -1;
}