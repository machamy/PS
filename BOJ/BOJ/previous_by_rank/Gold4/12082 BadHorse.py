import sys
input = sys.stdin.readline


def check(graph):
    color = {}
    
    for v in graph.keys(): 
        color[v] = 0
    
    for v in graph.keys():
        if color[v]:
            continue
        
        s = [v]
        while s:
            e = s.pop()
            c = 2 if color[e] == 1 else 1
            if not color[e]:
                color[e] = c
            for u in graph[e]:
                # 색칠이 안되어있으면 색칠
                if not color[u]:
                    color[u] = -color[e]
                    s.append(u)
                # 같은 색이면 False
                elif color[u] == color[e]:
                    return False
    return True

def solve():
    nPair = input().strip()
    graph = {}
    for _ in range(int(nPair)):
        a,b = input().split()
        if not a in graph:
            graph[a] = []
            graph[a].append(b)
        else:
            graph[a].append(b)
    
        if not b in graph:
            graph[b] = []
            graph[b].append(a)
        else:
            graph[b].append(a)
            

    return check(graph)

for i in range(int(input())):
    if solve():
        print(f"Case #{i}: Yes")
    else:
        print(f"Case #{i}: No")