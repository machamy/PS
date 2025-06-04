import sys
from collections import deque

input = sys.stdin.readline

N = 50

tree = [[] for _ in range(N+1)] #자식이 3개인 트리
# for i in range(1, N+1):
#     for j in range(3):
#         if i * 3 + j - 1<= N:
#             tree[i].append(i * 3 + j - 1)
# edges = []
# for i in range(1, N+1):
#     for j in tree[i]:
#         edges.append((i, j))
edges = []
while True:
    s = input()
    if s == '':
        break
    a, b = map(int, s.split())
    print(f'a: {a}, b: {b}')
    tree[a].append(b)
    tree[b].append(a)
    edges.append((a, b))



print(N, len(edges))
for i, j in edges:
    print(i, j)

colors = [0] * (N+1)
def dfs(prev_color, node):
    if colors[node] != 0:
        return
    c = prev_color
    colors[node] = c
    for child in tree[node]:
        c += 1
        if c > 4:
            c = 1
        dfs(c, child)

dfs(1, 1)

for i in range(1, N+1):
    if colors[i] == 0:
        colors[i] = 1
    print(colors[i], end=' ')