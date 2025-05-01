import sys

input = sys.stdin.readline

N,K,Q = map(int, input().split())

def get_parent(idx):
    return (idx - 2)//K + 1
#  P = (idx - 2)//K + 1
#  (idx+2)//K = P - 1
def get_depth(idx):
    if idx == 1:
        return 0
    idx -= 1
    depth = 1 
    while idx > 0:
        idx -= K ** depth
        depth += 1
    return depth - 1
    

def lca(a,b):
    res = 0
    ad = get_depth(a)
    bd = get_depth(b)
    if ad < bd:
        a,b = b,a
        ad,bd = bd,ad

    while(ad != bd):
        res += 1
        a = get_parent(a)
        ad = get_depth(a)
    
    while(a != b):
        res += 2
        a = get_parent(a)
        b = get_parent(b)

    return res
for _ in range(Q):
    a,b = map(int, input().split())
    if a == b:
        print(0)
        continue
    if K == 1:
        print(abs(a-b))
        continue
    print(lca(a,b))