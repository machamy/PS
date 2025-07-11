import sys

input = sys.stdin.readline

def solve():
    N,M = map(int,input().split())
    a,b,c = map(int,input().split())

    clouds = [[*map(int,input().split())] for _ in range(N)]
    
    prefix_sum = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for i in range(N):
        for j in range(M):
            prefix_sum[i][j] = clouds[i][j] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

    # for l in prefix_sum:
    #     print(l)
    ans = float('inf')
    def get_sum(a,b,i,j):
        return prefix_sum[i][j] - prefix_sum[a-1][j] - prefix_sum[i][b-1] + prefix_sum[a-1][b-1] 

    def formA(i,j):
        if N - i - a < 0 or M - j - (b+c) < 0: # 가로 b + c 세로 a
            return float('inf')
        return get_sum(i,j,i+a-1,j+b+c-1)
    def formB(i,j):
        if N - i - (a+b) < 0 or M - j - (c+a) < 0: # 가로 c + a 세로 a + b
            return float('inf')
        return get_sum(i,j,i+a-1,j+c-1) + get_sum(i+a,j+c,i+a+b-1,j+a+c-1)
    def formC(i,j):
        if N - i - (a+c) < 0 or M - j - (b+a) < 0: # 가로 b + a 세로 a + c
            return float('inf')
        return get_sum(i,j,i+a-1,j+b-1) + get_sum(i+a,j+b,i+a+c-1,j+a+b-1)
    
    for i in range(N):
        for j in range(M):
            res = [formA(i,j),formB(i,j),formC(i,j)]
            # print(res)
            ans = min(ans,min(res))
    print(ans)

solve()