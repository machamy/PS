
import sys
input = sys.stdin.readline

R,C = map(int,sys.stdin.readline().split())
D4 = [(0,1),(1,0),(0,-1),(-1,0)]

def solve():
    board = [list(sys.stdin.readline().strip()) for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'W':
                for dx,dy in D4:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<R and 0<=ny<C and board[nx][ny] == 'S':
                        print(0)
                        return
            else:
                if board[i][j] == '.':
                    board[i][j] = 'D'

    print(1)
    for i in range(R):
        print(''.join(board[i]))
        

solve()