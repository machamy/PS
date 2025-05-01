

N,M = map(int,input().split())
C = list(map(int,input().split()))
C.append(0)

dp = [[[-1 for _ in range(M+1)] for _ in range(11 + M)] for _ in range(N+1)]

def diff(a,b):
    if a <= b:
        return 0
    return (a-b)**2

def find(n,c,m): # n : 현재 일자, c : 사용 금액, m : 현재잔고
    if N == n:
        return 0
    print(f"{n=},{c=},{m=}")
    if dp[n][c][m] != -1:
        return dp[n][c][m]
    dp[n][c][m] = float("inf")
    for i in range(0, min(c+1,11)):
        dp[n][c][m] = min(dp[n][c][m], find(n+1,c - i, i) + diff(C[n] + m, C[n+1] + i))
    return dp[n][c][m]

print(find(1,M,0))