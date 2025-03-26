import sys
from heapq import heappush,heappop

input = sys.stdin.readline

def solve():
    N = int(input())
    R,D = map(int,input().split())
    M = int(input())
    builds = [list(map(int,input().split())) for _ in range(M)]
    adj = [list() for _ in range(N+1)]
    for h,t,E1,E2 in builds:
        for delta in range(0,N-h+1):
            adj[E1+delta].append((t,E2+delta))
            adj[E2+delta].append((t,E1+delta))
    # print(adj)
    dists = [float('inf') for _ in range(N+1)]
    q = [(0,R)]
    while(q):
        time, current = heappop(q)

        if dists[current] < time:
            continue
        for nxt_time, nxt in adj[current]:
            res_time = nxt_time + time
            if res_time < dists[nxt]:
                dists[nxt] = res_time
                heappush(q,(res_time,nxt))
                
    if dists[D] == float('inf'):
        print(-1)
    else:
        print(dists[D])
solve()