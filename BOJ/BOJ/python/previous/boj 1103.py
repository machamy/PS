import sys
from collections import deque, defaultdict

input = sys.stdin.readline
"""
형택이는 1부터 9까지의 숫자와, 구멍이 있는 직사각형 보드에서 재밌는 게임을 한다.

일단 보드의 가장 왼쪽 위에 동전을 하나 올려놓는다. 그다음에 다음과 같이 동전을 움직인다.

동전이 있는 곳에 쓰여 있는 숫자 X를 본다.
위, 아래, 왼쪽, 오른쪽 방향 중에 한가지를 고른다.
동전을 위에서 고른 방향으로 X만큼 움직인다. 이때, 중간에 있는 구멍은 무시한다.
만약 동전이 구멍에 빠지거나, 보드의 바깥으로 나간다면 게임은 종료된다. 형택이는 이 재밌는 게임을 되도록이면 오래 하고 싶다.

보드의 상태가 주어졌을 때, 형택이가 최대 몇 번 동전을 움직일 수 있는지 구하는 프로그램을 작성하시오.
"""


def solve():
    """
    dp 테이블로 앞으로 얼마나 갈 수 있는지 최대값 저장


    """
    N, M = map(int, input().split())

    board = [list(map(int, input().rstrip().replace("H", "0"))) for _ in range(N)]
    dp = [[-1 for _ in range(M)] for _ in range(N)]
    visit = [[False for _ in range(M)] for _ in range(N)]

    def dfs(i, j):
        if not (0 <= i < N and 0 <= j < M) or not board[i][j]:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if visit[i][j]:
            return float('inf')
        delta = board[i][j]
        visit[i][j] = True
        res = max(dfs(i + di * delta, j + dj * delta) for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)])
        res += 1
        visit[i][j] = False
        dp[i][j] = res
        if res:
            return res
        return -1

    if (ans := dfs(0, 0)) == float('inf'):
        return -1
    return ans


print(solve())
