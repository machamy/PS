import sys
input = sys.stdin.readline


# 
#

def solve():
    N,C = map(int,input().split())
    weights = [*map(int,input().split())]
    dp = [[0 for _ in range(C+1)] for _ in range(N+1)]

    dp[0][0] = 1
    
    result = 1
    for w in range(C):
        for i in range(0,N):
            if w + weights[i] <= C:
                dp[i+1][weights[i] + w] += dp[i][w] # insert
            dp[i+1][w] += dp[i][w] # no insert
            result += dp[i+1][w]

    
    print(result)
    for l in dp:
        print(l)

solve()