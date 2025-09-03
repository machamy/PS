import sys
input = sys.stdin.readline


def main():
    N = int(input())
    foods = list(map(int, input().split()))
    dp = [[[[float('inf') for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(N+1)]
    # dp[i][a][b][c] : i까지 생각했을때, a/b/c상태의 최소 횟수
    dp[0][0][0][0] = 0
    def dist(a,b):
        return min(abs(a-b), 10-abs(a-b))
    for i in range(0, N):
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    if dp[i][a][b][c] == float('inf'):
                        continue
                    # 음식필요 온도x
                    nxt = foods[i]
                    da = dist(a, nxt)
                    db = dist(b, nxt)
                    dc = dist(c, nxt)
                    dp[i+1][nxt][b][c] = min(dp[i+1][nxt][b][c], dp[i][a][b][c] + da)
                    dp[i+1][a][nxt][c] = min(dp[i+1][a][nxt][c], dp[i][a][b][c] + db)
                    dp[i+1][a][b][nxt] = min(dp[i+1][a][b][nxt], dp[i][a][b][c] + dc)
    ans = float('inf')
    for a in range(10):
        for b in range(10):
            for c in range(10):
                ans = min(ans, dp[N][a][b][c])
    print(ans)

main()  