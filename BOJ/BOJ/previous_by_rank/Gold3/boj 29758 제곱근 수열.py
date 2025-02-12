import sys

input = sys.stdin.readline


def solve():
    dp = [[-1 for _ in range(501)] for _ in range(70001)]

    # 하향식 DP
    def seq(n, l):
        if dp[n][l] != -1:
            return dp[n][l]
        if n == 1 and l == 1:
            return 1
        if n == 1 or l == 1:
            return 0
        raw_sqrt = n**0.5
        sqrt = int(raw_sqrt)
        if sqrt * sqrt == n:  # 1 4 16은 안됨
            sqrt -= 1
        dp[n][l] = 0
        for i in range(sqrt, 0, -1):
            dp[n][l] += seq(i, l - 1)
        return dp[n][l]

    for _ in range(int(input())):
        N, L = map(int, input().split())
        print(seq(N, L))


solve()
