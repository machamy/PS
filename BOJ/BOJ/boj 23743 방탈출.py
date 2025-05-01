import sys
import heapq
input = sys.stdin.readline


def solve():
    N,M = map(int,input().split())

    parents = [-1 for i in range(N+1)]
    # def union(x,y):
    #     x_root = find(x)
    #     y_root = find(y)
    #     if x_root == y_root:
    #         return
    #     if parents[x_root] < parents[y_root]:
    #         parents[y_root] = x_root
    #     elif parents[x_root] > parents[y_root]:
    #         parents[x_root] = y_root
    #     else:
    #         parents[x_root] = y_root
    #         parents[y_root] -= 1
        
    # def find(x):
    #     if parents[x]<0:
    #         return x
    #     parents[x] = find(parents[x])
    #     return parents[x]
    
    # edges = [None for _ in range(M)]
    # for i in range(M):
    #     u,v,c = map(int,input().split())
    #     edges[i] = (c,u,v)
    # for i,n in enumerate(map(int,input().split())):
    #     edges.append((n,0,i+1))
    
    # q = sorted(edges)
    # ans = 0
    # for edge in q:
    #     cost,u,v = edge
    #     # print(cost,u,v)
    #     if find(u) != find(v):
    #         union(u,v)
    #         ans += cost
    # print(ans)

    edges = [[] for _ in range(N+1)]
    for _ in range(M):
        u,v,c = map(int,input().split())
        edges[u].append((c,u,v))
        edges[v].append((c,v,u))
    for i,n in enumerate(map(int,input().split())):
        edges[0].append((n,0,i+1))
        edges[i+1].append((n,i+1,0))
    q = list(edges[0])
    heapq.heapify(q)
    ans = 0
    visited = [False for _ in range(N+1)]
    visited[0] = True
    while q:
        cost,u,v = heapq.heappop(q)
        if visited[v]:
            continue
        visited[v] = True
        for edge in edges[v]:
            if not visited[edge[2]]:
                heapq.heappush(q,edge)
        ans += cost
    print(ans)    
    


solve()