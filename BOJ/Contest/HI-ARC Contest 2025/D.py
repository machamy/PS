
A,B,C,D = map(int,input().split())

cnt = 0
dp = [[[[[-1 for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(5)]for _ in range(4)]
dp[0][0][0][0][0] = 1
dp[1][0][0][0][0] = 1
dp[2][0][0][0][0] = 1
dp[3][0][0][0][0] = 1
def solve(a,b,c,d,prev = -1):
    
    if dp[prev][a][b][c][d] != -1:
        return dp[prev][a][b][c][d]
    tmp = 0
    if a > 0 and prev != 0:
        tmp += solve(a-1,b,c,d,0)
    if b > 0 and prev != 1:
        tmp += solve(a,b-1,c,d,1)
    if c > 0 and prev != 2:
        tmp += solve(a,b,c-1,d,2)
    if d > 0 and prev != 3:
        tmp += solve(a,b,c,d-1,3)
    dp[prev][a][b][c][d] = tmp
    return dp[prev][a][b][c][d]

print(solve(A,B,C,D))