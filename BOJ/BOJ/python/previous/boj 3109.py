import sys

input = sys.stdin.readline

D3 = [(-1, 1), (0, 1), (1, 1)]


def solve():
    R, C = map(int, input().split())
    table = [list(input().rstrip()) for _ in range(R)]
    visit = [[0 for _ in range(C)] for _ in range(R)]


    def dfs(i, j):
        if j == C - 1:
            return 1

        for di, dj in D3:
            ni, nj = i + di, j + dj
            if not (0 <= ni < R and 0 <= nj < C):
                continue
            if visit[ni][nj] or table[ni][nj] == 'x':
                continue
            visit[ni][nj] = 1
            if dfs(ni, nj):
                return 1
        return 0

    result = 0
    for i in range(R):
        result += dfs(i, 0)

    print(result)


solve()
