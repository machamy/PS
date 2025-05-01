import sys

input = sys.stdin.readline

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    T = [None for _ in range(M)]
    Q = [None for _ in range(M)]
    for i in range(M):
        t,q = map(int,input().split())
        T[i] = t
        Q[i] = q

    q = 0
    A.sort()
    for i in range(M):
        day = T[i]
        condition = Q[i]
        # print(condition)
        while q < condition:
            if not A:
                print(-1)
                return 
            q += (day + A.pop())
    # print(q)
    while A:
        q += (T[-1] + A.pop())
    print(q)
    


solve()