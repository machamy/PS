import sys

input = sys.stdin.readline

def solve():
    N,M = map(int,input().split())

    adj = []

    for _ in range(M):
        a,b = map(int,input().split())
        adj.append((a,b))


    ans = 0
    visited = [False for _ in range(N+1)]
    def dfs(depth,cnt):
        nonlocal visited,ans
        if depth == M:
            ans = max(ans,cnt)
            return
        a,b = adj[depth]
        if visited[a] == False and visited[b] == False:
            visited[a] = True
            visited[b] = True
            dfs(depth + 1, cnt + 2)
            visited[a] = False
            visited[b] = False

        dfs(depth + 1, cnt)

        return cnt

    dfs(0,0)
        
    if ans < N:
        ans += 1

    print(ans)

solve()