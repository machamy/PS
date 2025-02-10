import sys

input = sys.stdin.readline
# 8 + 4 + 1 + 2 + 3 
def solve():
    N,M = map(int,input().split())
    arr = [*map(int,input().split())]
    sarr = []
    res = 0
    
    for sn in arr:
        tmp = sn % M
        if tmp == 0:
            res += 1
        else:
            sarr.append(tmp)
    s = sum(arr) % M
    if s == 0:
        print(N)
        return
    
    prev = [-1 for _ in range(M)]
    current = [-1 for _ in range(M)]
    prev[0] = 0
    max_remain = 0
    for i,sn in enumerate(sarr):
        for prev_remain in range(max_remain + 1):
            if prev[prev_remain] == -1:
                continue
            nxt_remain = (prev_remain+sn) % M
            max_remain = max(max_remain,nxt_remain)
            current[prev_remain] = max(current[prev_remain], prev[prev_remain])
            current[nxt_remain]  = max(current[nxt_remain], prev[prev_remain] + 1)
        prev,current = current,prev
    print(res + prev[0])


for _ in range(int(input())):
    solve()