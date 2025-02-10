import sys


input = sys.stdin.readline

N = 0
tree = [None] * 100001
left_children_cnt = [0] * 100001
right_children_cnt = [0] * 100001
left_node_cnt = [0] * 100001
right_node_cnt = [0] * 100001
visited = [False] * 100001
node_by_depth = [list() for _ in range(100001)]

def dfs(n):
    if n == -1:
        return 0
    l,r = tree[n]
    
    if not visited[n]:
        visited[n] = True
        left_children_cnt[n] += dfs(l)
        right_children_cnt[n] += dfs(r)
    
    return left_children_cnt[n] + right_children_cnt[n] + 1

def dfs_depth(prnt,n,is_right,depth):
    if n == -1:
        return
    l,r = tree[n]
    
    if is_right:
        # 오른쪽 자식인경우, 왼쪽 노드의 수 = 왼쪽 자식의 개수 + 부모의 왼쪽자식 + 부모
        left_node_cnt[n] = left_children_cnt[n] + left_node_cnt[prnt] + 1
        right_node_cnt[n] = N - left_node_cnt[n] - 1 # 자기자신 빼기
    else:
        # 왼쪽 자식인경우, 오른쪽 노드의 수 = 오른쪽 자식의 개수 + 부모의 오른쪽자식 + 부모
        # 왼쪽 노드의 수 = 부모의 왼쪽 노드의 수 - 자신의 오른쪽 자식의 개수 - 자신
        right_node_cnt[n] = right_children_cnt[prnt] + right_node_cnt[prnt] + 1
        left_node_cnt[n] = left_node_cnt[prnt] - right_children_cnt[n] - 1
    # print(f"n: {n} l: {left_node_cnt[n]} r: {right_node_cnt[n]}")
    # print(f"lc: {left_children_cnt[n]} rc: {right_children_cnt[n]}")
    # print(f"prnt: {prnt} l: {left_node_cnt[prnt]} r: {right_node_cnt[prnt]} d: {depth}")
    
    node_by_depth[depth].append(left_node_cnt[n]+1)
    
    dfs_depth(n,l,False,depth+1)
    dfs_depth(n,r,True,depth+1)

def solve():
    global N
    N = int(input())
    
    for _ in range(N):
        n,l,r = map(int, input().split())
        tree[n] = (l,r)
    
    for i in range(N):
        if not visited[i+1]:
            dfs(i+1)
    
    root = 0
    for i in range(1,N+1):
        if left_children_cnt[i] + right_children_cnt[i] + 1 == N:
            root = i
            break
   # print(f"root: {root} l: {left_children_cnt[root]} r: {right_children_cnt[root]}")
    
    left_node_cnt[root] = left_children_cnt[root]
    right_node_cnt[root] = right_children_cnt[root]
    
    dfs_depth(root,tree[root][0],False,2)
    dfs_depth(root,tree[root][1],True,2)
    ans_width = 1
    ans_depth = 1
    for depth in range(2,N+1):
        if not node_by_depth[depth]:
            break
        if len(node_by_depth[depth]) == 1:
            continue
        
        node_by_depth[depth].sort()
        width = node_by_depth[depth][-1] - node_by_depth[depth][0] + 1
        # print(f"d: {depth} l: {node_by_depth[depth][0]} r: {node_by_depth[depth][-1]}")
        # print(node_by_depth[depth])
        if width > ans_width:
            ans_width = width
            ans_depth = depth
    print(ans_depth, ans_width)
    
    
    


solve()