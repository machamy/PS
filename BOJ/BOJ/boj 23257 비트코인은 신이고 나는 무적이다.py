import sys

input = sys.stdin.readline

N,M = map(int,input().split())

"""


"""
nums = [abs(x) for x in map(int, input().split())]
dp = [[False for _ in range(1024)] for _ in range(M+1)]

for n in nums:
    x = abs(n)
    dp[1][x] = True

for m in range(1,M):
    for i in range(1024):
        if dp[m][i]:
            for n in nums:
                dp[m+1][i^n] = True
                print(f"{i} {m+1=} {i^n}")


for i in range(1023,-1,-1):
    if dp[M][i]:
        print(i)
        break