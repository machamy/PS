import sys
import bisect
from collections import defaultdict
input = sys.stdin.readline
#print = sys.stdout.write

def solve():
    N = int(input())
    
    lower = list()
    upper = []
    for e in input().split():
        n = int(e)
        if n <= 0:
            lower.append(-n)
        else:
            upper.append(n)
    lower.sort()
    L = defaultdict(int)
    amount = 0
    for e in lower:
        amount += 1
        L[e] += 1
    upper.sort(reverse=True)
    U = defaultdict(int)
    amount = 0
    for e in upper:
        amount += 1
        U[e] = amount
    ans = []
    LKeys = sorted(L.keys())
    UKeys = sorted(U.keys(),reverse=True)
    print(L)
    print(U)
    for a in range(N+1):
        n = L[bisect.bisect(LKeys,a)-1] + U[bisect.bisect_right(UKeys,a)]
        print(a,n)
        if a <= n:
            ans.append(str(a))
            
    print(str(len(ans)) + '\n')
    print(" ".join(ans))
solve()