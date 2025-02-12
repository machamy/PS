import sys
input = sys.stdin.readline
MAX_NUM = 2e9

def solve():
    N,M = map(int,input().split())
    values = [list(map(int,input().split())) for _ in range(N)]
    
    dp = [-MAX_NUM for _ in range(M)]
    left = [-MAX_NUM] * M
    right = [-MAX_NUM] * M
    dp[0] = values[0][0]
    right[0] = dp[0]
    for j in range(1,M):
        dp[j] = dp[j-1] + values[0][j]
        right[j] = dp[j]
    
    for i in range(1,N):
        left[M-1] = dp[M-1] + values[i][M-1]
        right[0] = dp[0] + values[i][0]
        for j in range(M-1,0,-1):
            left[j-1] = max(left[j], dp[j-1]) + values[i][j-1]

        for j in range(0,M-1):
            right[j+1] = max(right[j], dp[j+1]) + values[i][j+1]
            dp[j] = max(left[j],right[j])

        dp[-1] = max(left[-1],right[-1])


    print(right[-1])
solve()
    
