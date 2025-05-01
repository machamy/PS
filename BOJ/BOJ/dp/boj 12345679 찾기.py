
MOD = 1_000_000_007
# 12345679 찾기
# 5,7,8,9 로 나누어져야함
P = input().rstrip()
S = input().rstrip()

indexes = []
for i in range(len(S) - len(P) + 1):
    if S[i:i+len(P)] == P:
        indexes.append(i + 1)
# print(indexes)

dp = [[0 for _ in range(2520)] for _ in range(2)]
for i,index in enumerate(indexes):
    flag = i % 2
    prev = (i+1) % 2
    dp[flag] = [dp[prev][i] for i in range(2520)]
    dp[flag][index % 2520] += 1
    for i in range(2520):
        if dp[prev][i]:
            # print(i, dp[prev][i])
            n = (i * index) % 2520 
            dp[flag][n] = (dp[flag][n] + dp[prev][i]) % MOD
    # print("---")
    # print(dp[flag])
# for i in range(2520):
#     if dp[flag][i]:
#         print(i, dp[flag][i])
print(dp[int(len(indexes)%2 == 0)][0])
