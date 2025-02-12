import sys

input = sys.stdin.readline
print = sys.stdout.write

WALL = 'X'
BALL = 'L'
SPACE = '.'
name = ['오른','아래','왼','위']
D4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]



def solve():
    N, K = map(int, input().split())
    arr = [[*input().rstrip()] for _ in range(N)]
    cmds = [input()[0] for _ in range(K)]

    DP = [[[None for _ in range(N)] for _ in range(N)] for _ in range(4)]
    # 처음 공의 위치를 찾는다
    ball = []
    for i, l in enumerate(arr):
        for j, e in enumerate(l):
            if e == BALL:
                ball[:2] = i, j
                arr[i][j] = SPACE
                break
        else:
            continue
        break

    # 명령대로 회전시키고 중력을 적용한다
    current = 1
    for cmd in cmds:
        if cmd == "D":
            current -= 1
            if current < 0:
                current = 3
        elif cmd == "L":
            current += 1
            if current > 3:
                current = 0

        i, j = ball
        # 이미 연산한 결과가 있다면 사용
        if DP[current][i][j]:
            ball = DP[current][i][j]
            continue
        # 중력 적용
        while True:
            ni, nj = ball[0] + D4[current][0], ball[1] + D4[current][1]
            if not 0 <= ni < N or not 0 <= nj < N:
                break
            if arr[ni][nj] == WALL:
                break
            ball = [ni, nj]
        DP[current][i][j] = ball

    # 결과를 출력한다.
    arr[ball[0]][ball[1]] = BALL
    if current == 1:
        for l in arr:
            print("".join(l))
            print("\n")
        return
    if current == 3:
        for l in arr[::-1]:
            print("".join(l[::-1]))
            print("\n")
        return
    # 90도 오른쪽으로 돌린다.
    tmp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[j][N - 1 - i] = arr[i][j]
    arr = tmp
    if current == 0:
        for l in arr:
            print("".join(l))
            print("\n")
        return
    if current == 2:
        for l in arr[::-1]:
            print("".join(l[::-1]))
            print("\n")
        return


solve()