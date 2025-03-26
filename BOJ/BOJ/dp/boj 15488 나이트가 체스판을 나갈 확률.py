
N,x,y,K = map(int,input().split())
dp = [[[-1 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]

All = 8 ** K

D8 = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,+1), (-1,+2)]
def find(i,j,k):
    if i < 0 or i >= N or j < 0 or j >= N:
        return 0
    if dp[i][j][k] != -1:
        # print("f",i,j,k)
        return dp[i][j][k]
    if k == 0:
        # print(i,j)
        dp[i][j][k] = 1
        return 1
    res = 0
    for di,dj in D8:
        ni = i + di
        nj = j + dj
        res += find(ni,nj,k - 1)
    dp[i][j][k] = res
    return res


cnt = find(x-1,y-1,K)
s
# print(f"{cnt=}/{All=}")

print(cnt/All)
# for k in range(K+1):
#     for i in range(N):
#         for j in range(N):
#             print(dp[i][j][k], end= " ")
#         print()
#     print()