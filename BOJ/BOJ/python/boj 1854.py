import sys,heapq

input = sys.stdin.readline
inf = sys.maxsize
N,M,K = map(int,input().split())

edges = [list() for _ in range(N+1)]
ans = [[inf]*K for _ in range(N+1)]
for i in range(M):
    u,v,w = map(int,input().split())
    edges[u].append((v,w))

def dijk():
    q = [(0,1)]
    ans[1][0] = 0
    while q:
        cost, node = heapq.heappop(q)
        for nxt,distance in edges[node]:
            nxt_cost = cost + distance
            if nxt_cost < ans[nxt][K-1]:
                ans[nxt][K-1] = (nxt_cost)
                ans[nxt].sort()
                heapq.heappush(q,(nxt_cost,nxt))

dijk()
for i in range(1,N+1):
    if ans[i][K-1] == inf:
        print(-1)
    else:
        print(sorted(ans[i])[K-1])