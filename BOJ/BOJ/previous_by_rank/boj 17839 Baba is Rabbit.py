import sys
from collections import deque

input = sys.stdin.readline

graph = {}

def add_node(parent, child):
    if parent not in graph:
        graph[parent] = []
    graph[parent].append(child)

for _ in range(int(input())):
    parent, _is, child = input().split()
    add_node(parent, child)
    
#print(graph)
    
q = deque()
q.append("Baba")
visited = set()
while q:
    e = q.popleft()
    for nxt in graph.get(e, []):
        if nxt in visited:
            continue
        q.append(nxt)
        visited.add(nxt)
        
print(*sorted(visited), sep="\n")