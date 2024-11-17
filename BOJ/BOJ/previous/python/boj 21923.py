import sys

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    score_table = [list(map(int, input().split())) for _ in range(N)]

    # DP 테이블, 0 : 상승 1 : 하강
    DP = [[[None for _ in range(2)] for _ in range(M)] for _ in range(N)]

    # 상승 구간 계산
    DP[N - 1][0][0] = score_table[N-1][0]
    # 가장 왼쪽 열을 계산
    for i in range(N - 2, -1, -1):
        DP[i][0][0] = score_table[i][0] + DP[i + 1][0][0]
    # 가장 아래 행을 계산
    for j in range(1, M):
        DP[N-1][j][0] = DP[N-1][j - 1][0] + score_table[N-1][j]
    # 나머지 구역 계산
    for i in range(N - 2, -1, -1):
        for j in range(1, M):
            DP[i][j][0] = max(DP[i][j - 1][0], DP[i + 1][j][0]) + score_table[i][j]

    # 하강 구간 계산
    DP[0][0][1] = DP[0][0][0] + score_table[0][0]
    # 가장 윗 행 계산
    for j in range(1, M):
        DP[0][j][1] = max(DP[0][j][0], DP[0][j - 1][1]) + score_table[0][j]
    # 가장 왼쪽 행 계산
    for i in range(1, N):
        DP[i][0][1] = max(DP[i][0][0], DP[i-1][0][1]) + score_table[i][0]
    # 나머지 구역 계산
    for i in range(1, N):
        for j in range(1,M):
            DP[i][j][1] = max(DP[i][j][0], DP[i - 1][j][1], DP[i][j-1][1]) + score_table[i][j]

    print(DP[N-1][M-1][1])
solve()
