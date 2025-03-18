import sys

input = sys.stdin.readline

def solve():
    N,M = map(int,input().split())
    ans = 0
    flag = [input().rstrip() for _ in range(N)]
    ans += M - flag[0].count("W")
    ans += M - flag[-1].count("R")
    cnts =[[0,0,0] for _ in range(N)]
    for i in range(1, N-1):
        for j in range(M):
            if flag[i][j] == "W":
                cnts[i][0] += 1
            elif flag[i][j] == "B":
                cnts[i][1] += 1
            else:
                cnts[i][2] += 1
    dp = [[0,0,0] for _ in range(N)]
    dp[0] = [0,100,100]
    for i in range(1,N):
        # 흰색은 이전 흰 + 현재 빨파 개수
        dp[i][0] = dp[i-1][0] + cnts[i][1] + cnts[i][2] 
        # 파랑은 min(이전 흰 + 현재 흰파개수, 이전 파랑 + 현재 흰빨개수)
        dp[i][1] = min(dp[i-1][0] + cnts[i][0] + cnts[i][2]
                       , dp[i-1][1] + cnts[i][0] + cnts[i][2])
        # 빨강은 min(이전 파랑+현재 빨파개수, 이전 빨강+현재 흰파개수)
        dp[i][2] = min(dp[i-1][1] + cnts[i][0] + cnts[i][1]
                       , dp[i-1][2] + cnts[i][0] + cnts[i][1])
    print(ans + dp[N-1][2])

solve()