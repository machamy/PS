import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    values = list(map(int,input().split()))
    total = sum(values)

    # dp[k][j] 선배1 : k , 선배2 : j 만큼 효용일때 가능?
    dp = [[False for _ in range(total+1)] for _ in range(total+1)]
    dp[0][0] = True

    for i in range(N):
        v = values[i]
        for j in range(total,-1,-1):
            for k in range(total,-1,-1):
                if j-v >= 0:
                    # 첫 선배가 더 먹을 수 있는 경우
                    # 이전 값도 가능하면 이번에도 먹을 수 있다
                    # if dp[j-v][k] == True : dp[j][k] = True
                    dp[j][k] |= dp[j-v][k]
                if k-v >= 0:
                    # 두번쨰 선배가 더 먹을 수 있는 경우
                    # 이하생략
                    dp[j][k] |= dp[j][k-v]
                    
    res = 0
    # 모든 가능한 경우의 수에서 막내가 가장 적은 효용인 경우를 찾는다
    for i in range(total+1):
        for j in range (i+1): # a >= b 인 경우
            if dp[i][j] and j >= (c := total - i - j): # b >= c 인 경우
                res = max(res, c)
    print(res)
    return





solve()