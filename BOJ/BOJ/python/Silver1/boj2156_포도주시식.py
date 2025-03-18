import sys

input = sys.stdin.readline
'''
ooxoo
xooxo
oxoox
oxoxox

'''
def solve():
    N = int(input())
    data = [int(input()) for _ in range(N)]
    dp = [0] * N

    if N == 1:
        print(data[0])
        return
    if N == 2:
        print(sum(data[:2]))
        return
    dp[0] = data[0]
    dp[1] = data[0] + data[1]
    dp[2] = max(dp[1],data[1] + data[2], data[0]+data[2])
    if N == 3:
        print(dp[2])
        return
    for i in range(3,N):
        dp[i] = max(dp[i-3] + data[i-1] + data[i],
                     dp[i-2] + data[i],
                     dp[i-1]
                     )
    print(data)
    print(dp)
    print(max(dp[-3],dp[-2],dp[-1]))

solve()