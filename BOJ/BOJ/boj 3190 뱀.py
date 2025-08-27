import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    r,c = map(int,input().split())
    board[r-1][c-1] += 1

front = (0,0)
back = (0,0)
board[0][0] = -4
D4 = [(0,1), (1,0), (0,-1), (-1, 0)]
t = 0
d = 0
dback = 0
cmd = [input().split() for _ in range(int(input()))]
it = 0
while True:
    t += 1
    r,c = front
    
    # print(front)
    # print(back)
    # print(f"{t=}")
    if it < len(cmd) and cmd[it][0] == str(t-1):
        if cmd[it][1] == 'L':
            # 왼쪽
            d -= 1
            if d < 0:
                d += 4
        else:
            # 오른쪽
            d += 1
            if d >= 4:
                d -= 4
        it += 1
    
    nr,nc = r + D4[d][0], c + D4[d][1]
    if nr < 0 or nr >= N or nc < 0 or nc >= N:
        # print("out")
        break
    if board[nr][nc] < 0:
        # print("crash")
        break
    board[front[0]][front[1]] = d - 4
    if board[nr][nc] == 0:
        dback = board[back[0]][back[1]] + 4
        board[back[0]][back[1]] = 0
        back = (back[0] + D4[dback][0], back[1] + D4[dback][1])
    front = (front[0] + D4[d][0], front[1] + D4[d][1])
    

print(t)