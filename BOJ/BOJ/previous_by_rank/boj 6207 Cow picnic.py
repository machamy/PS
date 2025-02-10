import sys

sys.setrecursionlimit(10**7)

def solve():
    K,N,M = map(int, input().split())
    
    # K마리소
    # N개의 목초지
    # M개의 path
    
    cow_pos = [int(input()) for _ in range(K)]
    paths = [list() for _ in range(N+1)]
    
    for i in range(M):
        a,b = map(int, input().split())
        paths[a].append(b)
    
    cnts = [0 for _ in range(N+1)]
    res = 0
    def dfs(start, visited):
        nonlocal res
        visited[start] = True
        cnts[start] += 1
        if cnts[start] == K:
            res += 1
        for path in paths[start]:
            if not visited[path]:
                dfs(path, visited)
                
    for cow in cow_pos:
        visited = [False for _ in range(N+1)]
        dfs(cow, visited)
        
    print(res)

solve()