import sys
from collections import defaultdict,deque
sys.setrecursionlimit(40000)

def solve():
    n = int(input())

    tree = defaultdict(list)
    distances = [sys.maxsize] * (n + 1)
    parents = [None for _ in range(n + 1)]
    depths = [None for _ in range(n + 1)]
    visit = [False for _ in range(n + 1)]

    for i in range(n - 1):
        x, y, z = map(int, input().split())
        tree[x].append((y, z))
        tree[y].append((x, z))

    def bfs(start):
        q = deque()

        q.append([start, 0, 0])
        while q:
            node,distance,depth = q.popleft()

            distances[node] = distance
            depths[node] = depth
            for nxt, nxt_dist in tree[node]:
                if not visit[nxt]:
                    parents[nxt] = node
                    visit[node] = True
                    q.append([nxt, distance + nxt_dist, depths[node] + 1])

    def lca(a, b):
        if depths[b] < depths[a]:
            a,b = b,a
        while depths[b] != depths[a]:
            b = parents[b]

        if a == b:
            return a

        while a != b:
            a = parents[a]
            b = parents[b]
        return a

    visit[1] = True
    bfs(1)
    m = int(input())
    for i in range(m):
        x, y = map(int, input().split())
        print(distances[x] + distances[y] - 2 * distances[lca(x, y)])


solve()
