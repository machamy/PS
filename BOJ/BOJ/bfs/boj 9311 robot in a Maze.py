import sys
from collections import deque

input = sys.stdin.readline

def solve():
    R,C = map(int, input().split())
    maze = [input() for _ in range(R)]
    # print(maze)
    visited = [[False] * C for _ in range(R)]

    D4 = [(0,1), (1,0), (0,-1), (-1,0)]
    q = deque()
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'S':
                q.append((i,j,0))
                visited[i][j] = True
                break
        else:
            continue
        break

    while q:
        x,y,c = q.popleft()
        for dx,dy in D4:
            nx,ny = x+dx, y+dy
            nc = c + 1
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if maze[nx][ny] == 'G':
                    print("Shortest Path:",nc)
                    return
                elif maze[nx][ny] == 'O' or maze[nx][ny] == '0':
                    visited[nx][ny] = True
                    q.append((nx,ny,nc))
    else:
        print("No Exit")

for _ in range(int(input())):
    solve()