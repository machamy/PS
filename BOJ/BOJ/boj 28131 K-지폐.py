import sys
import heapq


input = sys.stdin.readline

def solve():
    N,M,K = map(int, input().split())
    S,T = map(int, input().split())

    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u,v,w = map(int, input().split())
        adj[u].append((v,w))
    
    q = []
    q.append((0,S))
    dist = [[float('inf') for _ in range(K)] for _ in range(N+1)]
    dist[S][0] = 0
    while q:
        cost, cur = heapq.heappop(q)
        if cost > dist[T][0]:
            continue

        for nxt, w in adj[cur]:
            new_cost = cost + w
            remain = new_cost % K
            if new_cost < dist[nxt][remain]:
                dist[nxt][remain] = new_cost
                heapq.heappush(q, (new_cost, nxt))
        
    if dist[T][0] == float('inf'):
        print("IMPOSSIBLE")
    else:
        print(dist[T][0])



solve()