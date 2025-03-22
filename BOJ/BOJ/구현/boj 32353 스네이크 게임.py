import sys
from collections import deque

input = sys.stdin.readline

# U R D L
D4 = [(-1,0),(0,1),(1,0),(0,-1)]

def solve():
    H,W,r0,c0,r1,c1 = map(int,input().split())

    world = [[*map(int,input().split())] for _ in range(H)] # 방향
    apple =  [[0 for _ in range(W)] for _ in range(H)] # 사과
    snake_data = [[0 for _ in range(W)] for _ in range(H)] # 현재 뱀 칸
    history = [[[0 for _ in range(4)] for _ in range(W)] for _ in range(H)] # 역사 추적용(snake_data로 합병 가능)

    dir = D4.index((r0-r1,c0-c1))
    snake = deque() # 왼쪽 머리, 오른쪽 꼬리
    snake.append((r0-1,c0-1))
    snake.append((r1-1,c1-1))
    snake_data[r0-1][c0-1] = 1
    # snake_data[r1-1][c1-1] = 1
    A = int(input())
    for _ in range(A):
        p,q = map(int,input().split())
        apple[p-1][q-1] = 1
    # age = 1
    while A:
        r,c = snake[0]
        # print('-- world --')
        # for l in world:
        #     print(l)
        # print('-- snake --')
        # for l in snake_data:
        #     print(l)
        # print("-- history --")
        # for l in history:
        #     print(l)
        if dir == (world[r][c] + 2) % 4: # 역방향
            pass
        else:
            dir = world[r][c]
        # print(dir, world[r][c])
        dr,dc = D4[dir]
        nr,nc = r+dr,c+dc # 다음 머리가 생길곳
        # print(f"{dir} {(r,c)=} {(nr,nc)=}")
        if nr < 0 or nr >= H or nc < 0 or nc >= W: # 맵밖이면 종료
            # snake.pop() # 꼬리하나 제거... 해야하는데 최대점수라서 상관없네
            # print("out field")
            break
        if snake_data[nr][nc]: # 충돌시 종료
            # print("collide")
            break
        if history[nr][nc][dir]:
            # print("loop")
            break
        # 앞으로 한칸 가기
        
        
        snake.appendleft((nr,nc))
        snake_data[nr][nc] = 1
        history[nr][nc][dir] = 1
        if apple[nr][nc] == 0 : # 사과 없음
            snake.pop()
            tr,tc = snake[-1] # 꼬리에는 안부딪힘
            snake_data[tr][tc] = 0
        else: # 사과 있음
            apple[nr][nc] = 0
            A -= 1
            # age *= 10
    
    print(len(snake))

solve()