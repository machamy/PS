import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())

    adj[a].append(b)
    adj[b].append(a)

for l in adj:
    l.sort()
# bfs로 하면, 자동으로 사전순으로 된다
visited = [False] * (N+1)
prev = [0] * (N+1)
S,E = map(int,input().split())

def bfs(S,E):
    q = deque([S])
    visited[S] = True
    while q:
        cur = q.popleft()

        for nxt in adj[cur]:
            if visited[nxt]:
                continue
            visited[nxt] =True
            q.append(nxt)
            prev[nxt] = cur

bfs(S,E)
def get_path(a,b):
    path = []
    current = b
    while current != a:
        path.append(current)
        current = prev[current]
    return path

path = get_path(S,E)
ans = 0
ans += len(path)
visited = [False] * (N+1)
for v in path:
    visited[v] = True

bfs(E,S)
path = get_path(E,S)
ans += len(path)

print(ans)