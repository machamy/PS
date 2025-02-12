import sys
from collections import deque

input = sys.stdin.readline
D4 = [(0,1),(1,0),(0,-1),(-1,0)]

N,M = map(int, input().split())
board = [[] for _ in range(N)]

start = None
pos1 = None
pos2 = None

for i in range(N):
    board_line = input().rstrip()
    for j in range(M):
        if board_line[j] == 'S':
            start = (i,j)
        elif board_line[j] == 'C':
            if pos1 is None:
                pos1 = (i,j)
            else:
                pos2 = (i,j)
    board[i] = board_line

visited = [[[[-1 for _ in range(M)] for _ in range(N)] for _ in range(4)] for _ in range(4)]
q = deque()
for dir in range(4):
    q.append((start,dir,0))
    visited[0][dir][start[0]][start[1]] = 0
ans = float('inf')

while q:
    (i,j),dir,pos_bit = q.popleft()
    cost = visited[pos_bit][dir][i][j]
    if pos_bit == 3:
        ans = min(ans,cost)
        break
    
    for nxt_dir,(di,dj) in enumerate(D4):
        nxt_pos_bit = pos_bit
        if nxt_dir == dir:
            continue
        ni,nj = i+di,j+dj
        if not (0<=ni<N and 0<=nj<M):
            continue
        if board[ni][nj] == '#':
            continue
        if board[ni][nj] == 'C':
            if (ni,nj) == pos1:
                nxt_pos_bit |= 1
            elif (ni,nj) == pos2:
                nxt_pos_bit |= 2

        if visited[nxt_pos_bit][nxt_dir][ni][nj] == -1:
            visited[nxt_pos_bit][nxt_dir][ni][nj] = cost + 1
            q.append(((ni,nj),nxt_dir,nxt_pos_bit))

if ans == float('inf'):
    print(-1)
else:
    print(ans)