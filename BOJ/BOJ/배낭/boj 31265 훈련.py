import sys

input = sys.stdin.readline
"""
일단 모든 날짜에 하나의 훈련은 들어가야함
그후 남은 훈련들로 M에 맞추면되는데... 이런식이면 BF고 시간초과날듯

단순하게 DP로 생각해보면...
dp[flag][m] -> 감당가능? (1<<1000) * 10000 ... 이건 아닌듯

문제를 좀 잘못이해한듯?
dp[m] = n : m의 시간을 n번까지 가능!


"""
def solve():
    N,M = map(int,input().split())
    trainings = list(map(int,input().split()))
    times = [list(map(int,input().split())) for _ in range(N)]

    dp = [-2 for _ in range(M+1)]
    dp[0] = -1
    # print(dp)
    for i in range(N):
        # print(f"--- {i} ---")
        for j in range(trainings[i]):
            time = times[i][j]
            for k in range(M,-1,-1):
                prev = k - time
                if prev >= 0 and (dp[prev] == i or dp[prev] == i-1): # 이전의 값이거나, 현재의 값
                    # print(f"{prev} -> {k}")
                    dp[k] = i
            # print(dp)
        # print(dp)
    # print(dp)
    for i in range(M, 0, -1): # 0의 경우는... 답이 없는거
        if dp[i] == N-1:
            print(i)
            return
    print(-1)

    # for i in range(N):
    #     for j in range(trainings[i]):
    #         time = times[i][j]
    #         for k in range(M+1):
    #             if dp[k] == i or dp[k] == i+1:
    #                 if k+time <= M:
    #                     dp[k+time] = i+1





solve()