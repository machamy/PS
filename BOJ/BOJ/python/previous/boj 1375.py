import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())

    adj = defaultdict(list)
    for _ in range(M):
        a, b = input().split()
        adj[b].append(a)

    def bfs(i):
        q = deque()
        q.append(i)

        visit = defaultdict(bool)
        res = set()
        while q:
            e = q.popleft()
            res.add(e)
            for nxt in adj[e]:
                if visit[nxt]:
                    continue
                visit[nxt] = True
                q.append(nxt)
        return res

    data = dict()

    result = []
    Q = int(input())
    for _ in range(Q):
        a, b = input().split()
        if a == b:
            result.append("gg")
            continue
        if a not in data:
            data[a] = bfs(a)
        if b not in data:
            data[b] = bfs(b)

        if b in data[a]:
            result.append(b)
        elif a in data[b]:
            result.append(a)
        else:
            result.append("gg")
    print(*result)


solve()
