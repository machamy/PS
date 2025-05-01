import sys

input = sys.stdin.readline

def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    R = [list(map(int,input().split())) for _ in range(K)]
    M = [list(map(int,input().split())) for _ in range(K)]
    ans = 0

    def dfs(day,rang,mary):
        nonlocal ans
        if day == K:
            ans = max(ans, mary + rang)
            return
        for i in range(N):
            if A[i] == 0:
                continue
            rr = rang + R[day][i]
            mm = mary
            A[i] -= 1
            for j in range(N):
                if A[j] == 0:
                    continue
                A[j] -= 1
                mm += M[day][j]
                dfs(day+1, rr, mm)
                mm -= M[day][j]
                A[j]+= 1
            A[i] += 1

    dfs(0, 0, 0)
    print(ans)

solve()