import sys

input = sys.stdin.readline
N = int(input())
target_scores = list(map(int, input().split()))
sums = [0]*(N+1)
sums[0] = target_scores[0]
for i in range(1,N):
    sums[i] = sums[i-1] + target_scores[i]

# dp[i] : 0~i까지 생각했을때, 최대점수
# dp[i] = max(i 표적 맞힌 점수, i 표적 맞히지 않은 점수)
# i번 표적을 맞힌다면, 상대는 dp[i-1]의 점수를 얻음
# i번 위의 표적을 맞히면, 상대는 i번 점수를 얻게됨
# 대신 dp[i-1]은 내거임
# 기권도 같은 경우임
dp = [None for _ in range(N+1)]
dp[0] = max(0,target_scores[0])

for i in range(1,N):
    dp[i] = max(sums[i] - dp[i-1], dp[i-1])

print(dp[N-1])