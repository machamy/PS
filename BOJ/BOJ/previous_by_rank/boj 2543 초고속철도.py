import sys

input = sys.stdin.readline
MOD = 20070713
sys.setrecursionlimit(20070713)
def find(arr,n,l,r = -1):
    l = l
    r = len(arr) if r == -1 else r
    while l < r:
        mid = (l+r) // 2
        if arr[mid][0] <= n:
            l = mid + 1
        else:
            r = mid
    return l

def chk(robots, N, dp, i):
    if N == i:
        return 1
    if dp[i] != -1:
        return dp[i]
    install = chk(robots, N, dp, i+1) % MOD
    not_intall = chk(robots, N, dp, find(robots,robots[i][1],i+1)) % MOD
    dp[i] = (install + not_intall) % MOD
    return dp[i]

def solve():
    N = int(input())
    robots = [list(map(int,input().split())) for _ in range(N)]
    robots.sort()

    dp = [-1 for _ in range(N)]
    print(chk(robots,N,dp,0))


solve()