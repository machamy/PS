

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

dp = [[-1]*(M+1) for _ in range(N+1)]
route = [[None]*(M+1) for _ in range(N+1)]

def LCIS(a_begin,b_begin):
    if dp[a_begin][b_begin] != -1:
        return dp[a_begin][b_begin]
    dp[a_begin][b_begin] = 1

    for i in range(a_begin+1,N):
        if A[i] <= A[a_begin]:
            continue
        for j in range(b_begin+1,M):
            if A[i] != B[j]:
                continue
            cnt = LCIS(i,j) + 1 # 이후 지점중 하나부터의 최장 공통 증가 부분 수열의 길이
            if dp[a_begin][b_begin] < cnt:
                dp[a_begin][b_begin] = cnt
                route[a_begin][b_begin] = (i,j)
            break
    return dp[a_begin][b_begin]


def get_route(ans_pos):
    si,sj = ans_pos
    print(A[si],end=' ')
    if route[si][sj] == None:
        return
    
    get_route(route[si][sj])

ans_cnt = 0
ans_pos = None
for i in range(N):
    for j in range(M):
        if A[i] != B[j]:
            continue
        cnt = LCIS(i,j)
        if ans_cnt < cnt:
            ans_cnt = cnt
            ans_pos = (i,j)
        break



print(ans_cnt)
if ans_cnt > 0:
    get_route(ans_pos)