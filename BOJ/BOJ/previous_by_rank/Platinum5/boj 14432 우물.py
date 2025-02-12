import sys

input = sys.stdin.readline

def solve():
    # 마을, 길 의 수
    N,M = map(int,input().split())

    needs = list(map(int,input().split()))
    roads = [list() for _ in range(N)]

    for _ in range(M):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        roads[a].append(b)
        roads[b].append(a)
    
    # 1. 현재 노드에 우물을 짓기
    # 2. 자식 노드에 우물을 짓기
    # 중에서 더 적은 비용...
    # 리프 노드면, 다른 노드에 짓는게 맞음
    # 리프의 부모에 지으면, 그건 또다른 리프가 됨
    ans = 0

    def dfs(node,parent):
        nonlocal roads, needs, ans
        max_needs = 0
        for nxt in roads[node]:
            if nxt == parent:
                continue
            dfs(nxt,node)
            max_needs = max(max_needs,needs[nxt])
        build(node,max_needs)

    def build(node,amount):
        nonlocal roads, needs, ans
        needs[node] -= amount
        for nxt in roads[node]:
            needs[nxt] -= amount
        ans += amount

    dfs(0,-1)
    ans += max(0,needs[0])
    print(ans)

solve()