import sys
from collections import deque

def solve():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    origin = sorted(A)
    D = dict()
    for i,e in enumerate(origin):
        D[e] = i
    deques = []
    
    for a in A:
        ok = False
        for dq in deques:
            if ok:
                break
            if D[dq[0]] == D[a] + 1 :
                dq.appendleft(a)
                ok = True
            elif D[dq[-1]] == D[a] - 1 :
                dq.append(a)
                ok = True
        if not ok:
            deques.append(deque([a]))
    
    print(len(deques))

solve()