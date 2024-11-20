import sys
input = sys.stdin.readline

D4 = [(1,0),(-1,0),(0,1),(0,-1)]
def solve():
    N,M = map(int,input().split())
    world = [[*map(int,input().split())] for _ in range(N)]
    graphs = set()
    island_count = 0

    def get(tp):
        nonlocal world
        return world[tp[0]][tp[1]]

    def add_edge(a,b,cost):
        nonlocal graphs
        if b > a:
            a,b = b,a
        graphs.add((a,b,cost))

    def make_island(i,j):
        nonlocal world
        island_count += 1
        s = [(i,j)]
        while s:
            i,j = s.pop()
            world[i][j] = island_count+10
            for di,dj in D4:
                ni,nj = i+di,i+dj
                if ni < 0 or ni >= N or nj < 0 or nj > M:
                    continue
                s.append((ni,nj))

    prtns = [i for i in range(6)]
    def union(a,b):
        nonlocal prnts
    
    def find(a):
        nonlocal prnts

    
    vertical_prev = [None for _ in range(N)]
    for i in range(N):
        horizontal_prev = None
        for j in range(M):
            if world[i][j] == 1:
                make_island(i,j)
            if world[i][j] > 1:
                # 현재 위치에 섬이 있음
                if horizontal_prev:
                    # 이전 섬이 있으면(가로)
                    if get(i) == world[i][j]:
                        # 같으면 이전 j 갱신
                        horizontal_prev = j
                    else:
                        # 다르면 간선 추가 및 갱신
                        add_edge(world[i][j],get(i),abs(horizontal_prev - j))
                        horizontal_prev = j
                else:
                    horizontal_prev = j

                if vertical_prev[j]:
                    # 이전 섬이 있으면(세로)
                    if get(i) == world[i][j]:
                        # 같으면 이전 j 갱신
                        horizontal_prev = j
                    else:
                        # 다르면 간선 추가 및 갱신
                        add_edge(world[i][j],get(i),abs(horizontal_prev - j))
                        horizontal_prev = j
                else:
                    vertical_prev = i
