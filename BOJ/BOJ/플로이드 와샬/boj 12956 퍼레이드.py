import sys

input = sys.stdin.readline

def debug_print(matrix):
    for row in matrix:
        print(*row)

def solve():
    N,M = map(int, input().split())
    adj = [[float('inf')] * (N) for _ in range(N)]
    roads = [list(map(int, input().split())) for _ in range(M)]
    for i in range(M):
        fr,to, time = roads[i]
        adj[fr][to] = time
        adj[to][fr] = time

    initial =  [[adj[i][j] for j in range(N)] for i in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if initial[i][k] + initial[k][j] < initial[i][j]:
                    initial[i][j] = initial[i][k] + initial[k][j]
    ans = [0] * (M)
    # debug_print(initial)

    for ban_road in range(M):
        # print(f"---- ban_road {ban_road} ---")
        dist = [[float('inf')] * (N) for _ in range(N)]
        for r in range(M):
            fr,to,time = roads[r]
            dist[fr][to] = time
            dist[to][fr] = time
            # print(f"fr {fr} to {to} time {time}")
        dist[roads[ban_road][0]][roads[ban_road][1]] = float('inf')
        dist[roads[ban_road][1]][roads[ban_road][0]] = float('inf')
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    
        cnt = 0
        for i in range(N):
            for j in range(i+1, N):
                # if initial[i][j] == float('inf'):
                #     continue  
                if dist[i][j] != initial[i][j]:
                    cnt += 1
        ans[ban_road] = cnt
        
        # debug_print(dist)
    
    print(*ans)

solve()