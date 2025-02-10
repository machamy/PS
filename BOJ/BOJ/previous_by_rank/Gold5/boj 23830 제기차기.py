import sys


def solve(N,A,p,q,r,S):
    arr = sorted(A)
    # score > K + r 이면, A[i] -= p
    # score < K     이면, A[i] += q 
    
    m,M = 1, 1_000_001
    s,e = m,M
    ans = sys.maxsize
    while s <= e:
        K = (s+e) // 2
        total = 0
        #print(f"{s=},{e=} , {K=}")
        for a in A:
            if a > K + r:
                total += a - p
            elif a < K:
                total += a + q
            else:
                total += a
        #    print(f"{total=}")

       # print(f"{total=}  {S}")
        if total >= S:
            ans = min(ans,K)
            e = K - 1
        else:
            s = K + 1


    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)


    
    
    




N = int(input())
A = [*map(int,input().split())]
p,q,r,S = map(int,input().split())
solve(N,A,p,q,r,S)