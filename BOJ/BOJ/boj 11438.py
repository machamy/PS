import sys
from collections import defaultdict, deque

input = sys.stdin.readline
sys.setrecursionlimit(100_100)

def solve():
    n = int(input())

    tree = defaultdict(list)
    parents = [[0 for _ in range(20)] for _ in range(n + 1)]
    depths = [0 for _ in range(n + 1)]
    visit = [False for _ in range(n + 1)]

    for i in range(n - 1):
        x, y = map(int, input().split())
        tree[x].append(y)
        tree[y].append(x)

    def dfs(node, prnts):
        depths[node] = depths[prnts] + 1
        parents[node][0] = prnts

        for i in range(1, 17):
            tmp = parents[node][i - 1]
            parents[node][i] = parents[tmp][i - 1]

        for i in range(len(tree[node])):
            tmp = tree[node][i]
            if tmp != prnts:
                dfs(tmp, node)

    def lca(a, b):
        if depths[b] < depths[a]:
            a, b = b, a

        for i in range(16, -1, -1):
            if depths[a] <= depths[parents[b][i]]:
                b = parents[b][i]

        if a == b:
            return a

        ans = a
        for i in range(16, -1, -1):
            if parents[a][i] != parents[b][i]:
                a = parents[a][i]
                b = parents[b][i]
            ans = parents[a][i]

        return ans

    visit[1] = True
    dfs(1, 0)
    m = int(input())
    for i in range(m):
        x, y = map(int, input().split())
        print(lca(x, y))


solve()
