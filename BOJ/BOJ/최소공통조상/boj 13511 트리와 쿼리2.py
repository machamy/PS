import sys

input = sys.stdin.readline
write = sys.stdout.write
print = lambda x : write(str(x)+"\n")
sys.setrecursionlimit(100_010)
def solve():
    N = int(input())
    MAX_DEPTH = 18

    edges = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        edges[u].append((v,w))
        edges[v].append((u,w))

    root_costs = [0 for _ in range(N+1)]
    parents = [[0 for _ in range(MAX_DEPTH)] for _ in range(N+1)]
    depths = [-1 for _ in range(N+1)]
    # 1번 노드를 루트로 하는 트리를 생각
    def dfs(current,parent):
        depths[current] = depths[parent] + 1
        parents[current][0] = parent

        for i in range(1,MAX_DEPTH):
            prev_parent = parents[current][i-1]
            parents[current][i] = parents[prev_parent][i-1]

        for nxt,weight in edges[current]:
            if depths[nxt] == -1:
                root_costs[nxt] = root_costs[current] + weight
                dfs(nxt,current)
    def lca(a,b):
        if depths[a] > depths[b]:
            a,b = b,a
        # b가 a보다 깊음

        for i in range(MAX_DEPTH-1,-1,-1):
            if depths[a] <= depths[parents[b][i]]:
                # b를 끌어올림
                b = parents[b][i]
        if a == b:
            return a
        
        for i in range(MAX_DEPTH-1,-1,-1):
            if parents[a][i] == parents[b][i]:
                continue
            a = parents[a][i]
            b = parents[b][i]
        return parents[a][0]
    dfs(1,0)

        
    # print(depths)
    # print(parents)
    # print(root_costs)

    # 분기가 없으면 점프 뛸 수 있도록 하는거?
    Q = int(input())
    for _ in range(Q):
        cmd, *args = map(int,input().split())
        if cmd == 1:
            a,b = args
            p = lca(a,b)
            print(root_costs[a] + root_costs[b] - root_costs[p]*2)
        else:
            #k번째 정점 출력
            a,b,k = args
            p = lca(a,b)
            
            
            parent_distance = depths[a] - depths[p] + 1 # 자기자신은 1번째
            
            if parent_distance == k:
                print(p)
                continue
            
            if parent_distance > k:
                k -= 1
                res = a
                for i in range(MAX_DEPTH-1,-1,-1):
                    if k >= (1 << i):
                        k -= (1<<i)
                        res = parents[res][i]

                        
                print(res)
            else:
                k -= parent_distance # 위에서부터의 거리
                k = depths[b] - depths[p] - k# 전체거리 - 위에서부터 거리
                # print(parent_distance,k,b)
                res = b
                for i in range(MAX_DEPTH-1,-1,-1):
                    if k >= (1 << i):
                        k -= (1<<i)
                        res = parents[res][i]
                        
                print(res)
solve()