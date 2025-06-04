import sys

input = sys.stdin.readline

def solve():
    n,m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    colors = [0] * (n+1)

    def dfs(node, color):
        colors[node] = color
        flag = True
        for neighbor in adj[node]:
            if colors[neighbor] == 0:
                flag = dfs(neighbor, -color)
                if not flag:
                    return False
            elif colors[neighbor] == color:
                return False
        return flag
    
    for i in range(1, n+1):
        if colors[i] == 0:
            res = dfs(i, 1)
            if not res:
                print("impossible")
                return
    else:
        print("possible")
        return


for _ in range(int(input())):
    solve()