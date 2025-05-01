import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

MAX = 1_000
"""
3 5 8
33 35 38 53 55 58 83 85 88
333 335 338 353 355 358 383 385 388 533 535 538 553 555 558 583 585 588 833 835 838 853 855 858
"""
dp = [None for _ in range(MAX+1)]
# print('3'*cnt[0] + '5'*cnt[1] + '8'*cnt[2])
dp[3] = [1,0,0]
dp[5] = [0,1,0]
dp[8] = [0,0,1]
for i in range(3, MAX+1):
    if dp[i] is None:
        continue
    for delta in [3,5,8]:
        if i + delta <= MAX:
            tmp = [0,0,0]
            tmp[0] = dp[i][0] + (delta == 3)
            tmp[1] = dp[i][1] + (delta == 5)
            tmp[2] = dp[i][2] + (delta == 8)
            if dp[i+delta] is None:
                dp[i+delta] = tmp
            if sum(tmp) < sum(dp[i+delta]):
                dp[i+delta] = tmp

# for i in range(21):
#     print(i, dp[i])

def solve():
    N = int(input())
    if sum(dp[N]) < 0:
        print(-1)
        return

    cnt = dp[N]
    print('3'*cnt[0] + '5'*cnt[1] + '8'*cnt[2])


for _ in range(int(input())):
    solve()