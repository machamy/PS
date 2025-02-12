import sys

input = sys.stdin.readline

def solve():
    N,M = map(int,input().split())
    direction = 'L'
    def change(x):
        nonlocal direction
        if x == '1':
            if direction == 'L':
                return -1
            return 1
        return 0
    sums = [0] * M
    birds = [None for _ in range(N)]
    for i in range(N):
        direction, nums = input().split()
        
        sound = list(map(change,nums))
        birds[i] = sound
        for j in range(M):
            sums[j] += sound[j]

    res = sys.maxsize
    kill_idx = 0
    for i in range(N):
        total, Max = 0, 0
        for j in range(M):
            total += sums[j] - birds[i][j]
            Max = max(Max,abs(total))
        if Max < res:
            kill_idx = i
            res = Max

    print(kill_idx+1)
    print(res)
solve()
