import sys,heapq

input = sys.stdin.readline
inf = sys.maxsize
N,M,K = map(int,input().split())

edges = [list() for _ in range(N+1)]
ans = [[] for _ in range(N+1)]
for i in range(M):
    u,v,w = map(int,input().split())
    edges[u].append((v,w))

def dijk():
    q = [(0,1)]
    ans[1].append(0)
    while q:
        cost, node = heapq.heappop(q)
        for nxt,distance in edges[node]:
            nxt_cost = cost + distance
            if len(ans[nxt]) < K:
                ans[nxt].append(-nxt_cost)
                heapq.heappush(q,(nxt_cost,nxt))
                if len(ans[nxt]) == K:
                    heapq.heapify(ans[nxt])
            else:
                if nxt_cost < -ans[nxt][0]:
                    heapq.heappop(ans[nxt])
                    heapq.heappush(ans[nxt],-nxt_cost)
                    heapq.heappush(q,(nxt_cost,nxt))

dijk()
for i in range(1,N+1):
    if len(ans[i]) < K:
        print(-1)
    else:
        print(-ans[i][0])