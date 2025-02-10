import sys

sys.setrecursionlimit(11000)
input = sys.stdin.readline
N = int(input())
initial = list(map(int, input().strip()))
target = list(map(int, input().strip()))
dp = [[-1] * 10 for _ in range(N)]
turn_arr = [[-1] * 10 for _ in range(N)]
 
def next(lv, left_turn):
    if lv == N:
        return 0
    if dp[lv][left_turn] != -1:
        return dp[lv][left_turn]
    left_cost = (target[lv] - (initial[lv] + left_turn)) % 10
    right_cost = 10 - left_cost
    nxt_left_turn = (left_turn + left_cost) % 10

    L = left_cost + next(lv+1,nxt_left_turn)
    R = right_cost + next(lv+1,left_turn)
    if L < R:
        dp[lv][left_turn] = L
        turn_arr[lv][left_turn] = left_cost
    else:
        dp[lv][left_turn] = R
        turn_arr[lv][left_turn] = -right_cost
                                 
    return dp[lv][left_turn]


print(next(0,0))
left_turn = 0
for i,e in enumerate(turn_arr):
    turn = turn_arr[i][left_turn]
    print(i+1,turn)
    if turn > 0:
        left_turn = (left_turn + turn) % 10