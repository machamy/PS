import sys

sys.setrecursionlimit(11000)
input = sys.stdin.readline
N = int(input())
initial = list(map(int, input().strip()))
target = list(map(int, input().strip()))
dp = [[-1] * 10 for _ in range(N)]
 
def next(lv, left_turn):
    if lv == N:
        return 0
    if dp[lv][left_turn] != -1:
        return dp[lv][left_turn]
    left_cost = (target[lv] - (initial[lv] + left_turn + 10) + 10) % 10
    right_cost = 10 - left_cost
    nxt_left_turn = (left_turn + left_cost) % 10

    dp[lv][left_turn] = min(left_cost + next(lv+1,nxt_left_turn),
                                 right_cost + next(lv+1,left_turn))
    return dp[lv][left_turn]


print(next(0,0))