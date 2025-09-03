import sys

input = sys.stdin.readline

dp = [0 for _ in range(10_001)]
dp[0] = 1


for i in range(1, 10_001):
    dp[i] = dp[i - 1]

for i in range(2, 10_001):
    dp[i] += dp[i - 2]

for i in range(3, 10_001):
    dp[i] += dp[i - 3]


for _ in range(int(input())):
    n = int(input())
    print(dp[n])