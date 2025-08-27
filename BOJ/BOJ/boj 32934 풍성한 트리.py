import sys
from collections import deque

def solve():
    N = int(input())
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    
    leafs = []
    for node,e in enumerate(edges):
        if len(e) == 1:
            leafs.append(node)
            continue
        if len(e) != 3:
            print(-1)
            return
        
    visited = [0 for _ in range(N)]
    for l in leafs:
        visited[l] = True
    q = deque(leafs)
    current_cycle = 1
    ans = -1
    while q:
         q_size = len(q)
         if q_size == 1:
             ans = q.pop()
             break
         for _ in range(q_size):
             node = q.popleft()
             for nxt in edges[node]:
                 if visited[nxt]:
                     continue
                 visited[nxt] = True
                 q.append(nxt)
    else:
        print(-1)
        return
        
    print(1)
    print(ans+1)
    
    

solve()