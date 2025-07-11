import sys

input = sys.stdin.readline

'''
0,0 루트
-1,0 1,0 위 아래


'''
dp = [[[-1 for _ in range(30)] for _ in range(30)] for _ in range(30)]

def get_adj(i,j):
    res = [(i-1,j),(i+1,j)]
    if j % 2 == 1:
        res.append((i,j+1))
        res.append((i+1,j+1))
        res.append((i,j-1))
        res.append((i+1,j-1))
    else:
        res.append((i-1,j+1))
        res.append((i,j+1))
        res.append((i-1,j-1))
        res.append((i,j-1))
    return res


def dfs(remain,i,j):
    if remain == 0:
        if i == 14 and j == 14:
            return 1
        else:
            return 0
    if dp[remain][i][j] != -1:
        return dp[remain][i][j]
    res = 0
    for ni,nj in get_adj(i,j):
        res += dfs(remain-1,ni,nj)
    dp[remain][i][j] = res
    return dp[remain][i][j]

def main():
    N = int(input())
    ans = dfs(N,14,14)
    print(ans)


for _ in range(int(input())):
    main()