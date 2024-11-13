import sys
input = sys.stdin.readline


def solve():
    N,Q = map(int,input().split())
    tree = [0] * ((N*2))
    arr = [*map(int,input().split())]
    init(tree,arr,1,0,N-1)

    for i in range(Q):
        x,y,a,b = map(int,input().split())
        print(getSum(tree,x,y))
        setNum(tree,a,b)
    
def init(tree,arr,node,a,b):
    if a == b:
        # print(a,arr)
        tree[node] = arr[a]
        return
    mid = (a+b)//2
    print(node)
    init(tree,arr,node*2,a,mid)
    init(tree,arr,node*2+1,mid+1,b)
    tree[node]=tree[node*2]+tree[node*2+1]

# l,r : 노드의 범위
# a,b 검색범위
def getSum(tree,node,a,b,l,r):
    if a <= l and r <= b:
        return tree[node]
    if l < a or b < r:
        return 0
    return sum(getSum(tree,node*2,a,(a+b)//2,l,r),
               getSum(tree,node*2+1,(a+b)//2+1,b,l,r))

def setNum(t,arr,i,n):
    diff = n - arr[i]
    a[i] = n
    update(t,0)
    return

def update(t,node,i,diff,a,b):
    if i < a or i > b:
        return
    tree[node] += diff
    if a!=b:
        update(t,node*2,diff,a,(a+b)//2)
        update(t,node*2+1,i,diff,(a+b)//2 + 1,b)

solve()