import sys

input = sys.stdin.readline
write = sys.stdout.write

def parse_input():
    s,e = input().split(" - ")
    start = get_idx(*map(int,s.split(":")))
    end = get_idx(*map(int,e.split(":")))
    return start,end

def get_idx(h,m,s):
    return h*3600+m*60+s

def query(l,r,node=1,start=0,end=86400-1):
    """
    l: 최초 쿼리의 왼쪽 끝
    r: 최초 쿼리의 오른쪽 끝
    node: current node
    start: 현재 노드의 왼쪽
    end: 현재 노드의 오른쪽
    """
    update_lazy(node,start,end) 
    if l>end or r<start:
        return -1
    if l<=start and end<=r:
        return tree[node]
    mid = (start+end)//2
    left = query(l,r,node*2,start,mid)
    right = query(l,r,node*2+1,mid+1,end)
    if left == -1:
        return right
    elif right == -1:
        return left
    return left+right

def update_range(l,r,diff,node=1,start=0,end=86400-1):
    update_lazy(node,start,end)
    if l>end or r<start:
        return
    if l <= start and end <= r:
        tree[node] += (end-start+1)*diff
        # 완벽하게 포함되면, 하위 노드는 나중에 갱신하자
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    mid = (start+end)//2
    update_range(l,r,diff,node*2,start,mid)
    update_range(l,r,diff,node*2+1,mid+1,end)
    tree[node] = tree[node*2]+tree[node*2+1]

def update_lazy(node,start,end):
    if lazy[node] != 0:
        tree[node] += (end-start+1)*lazy[node]
        if start != end:
            # 리프 노드가 아니면, 자식 노드에게 lazy 전파
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0



N = int(input())
# arr = [0]*86400
tree = [0] * ((1 << ((86400).bit_length()+1)) + 1)
lazy = [0] * len(tree)
# print(((86400).bit_length()+1))
for _ in range(N):
    s,e = parse_input()
    if e < s:
        update_range(0,e,1)
        update_range(s,86400-1,1)
    else:
        update_range(s,e,1)

for _ in range(int(input())):
    s,e = parse_input()
    total = 0
    delta = 1
    if e < s:
        total = query(0,e)+query(s,86400-1)
        delta = e + 86400 - s + 1
    else:
        total = query(s,e)
        delta = e-s + 1
    write(f"{total/(delta):.10f}\n")