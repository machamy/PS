import sys

input = sys.stdin.readline
possibles = list(map(int, input().split()))
possibles.sort()


def dp_func(dp, x, y, is_a_turn=True):
    turn = 0 if is_a_turn else 1
    if dp[turn][x][y] != -1:
        return dp[turn][x][y]

    for p in possibles:
        if 0 <= x - p and not dp_func(dp, x - p, y, not is_a_turn):
            dp[turn][x][y]= 1
            return 1
        if 0 <= y - p and not dp_func(dp, x, y - p, not is_a_turn):
            dp[turn][x][y] = 1
            return 1
    
    dp[turn][x][y] = 0
    return 0

def solve(possibles):
    x,y = map(int, input().split())
    dp = [[[-1 for _ in range(501)] for _ in range(501)] for _ in range(2)]

    if dp_func(dp, x, y):
        print("A")
    else:
        print("B")







for _ in range(5):
    solve(possibles)