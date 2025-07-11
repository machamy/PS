
N, M = map(int,input().split())
A = " "+input()
B = " "+input()

# if len(B) < len(A):
#     A,B = B,A

"""
aaabb
aabbb

aaabbd
aaabcd
"""

dp = [[0] * (M + 1) for _ in range(N + 1)]

def dist(a,b):
    return abs(ord(a)-ord(b))

for i in range(1, N+1):
    dp[i][1] = dp[i-1][1] + dist(A[i],B[1])
for j in range(1, M+1):
    dp[1][j] = dp[1][j-1] + dist(A[1],B[j])
for i in range(2, N + 1):
    for j in range(2, M + 1):
            dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) \
                    + dist(A[i], B[j])
for l in dp:
    print(l)
print(dp[-1][-1])