import sys
sys.setrecursionlimit(10000)
N = int(input())
W = int(input())
crimes = [list(map(int,input().split())) for _ in range(W)]
dp = [[-1 for _ in range(W+1)] for _ in range(W+1)] #[A][B]일때 거리
trace = [[-1 for _ in range(W+1)] for _ in range(W+1)] # 경로 역추적
def distance(p,q):
    a,b = p
    i,j = q
    return abs(a-i) + abs(b-j)

"""
1 2 3 4 5 6 7 

A는 A[i-1]

"""

def recursive(a,b):
    if a == W - 1 or b == W - 1:
        return 0
    if dp[a+1][b+1] != -1:
        return dp[a+1][b+1]
    nxt_crime = max(a,b) + 1
    a_pos = (1,1) if a == -1 else crimes[a]
    b_pos = (N,N) if b == -1 else crimes[b]
    # 경찰차의 현재 위치에서, 범죄지로의 거리
    d_a = distance(a_pos,crimes[nxt_crime]) 
    d_b = distance(b_pos,crimes[nxt_crime])

    # 재귀로 최종 비용 가져오기
    cost_a = d_a + recursive(nxt_crime,b)
    cost_b = d_b + recursive(a,nxt_crime)
    if cost_a < cost_b:
        trace[a+1][b+1] = 1
        dp[a+1][b+1] = cost_a
    else:
        trace[a+1][b+1] = 2
        dp[a+1][b+1] = cost_b
    # print(f"{a+1} {b+1} {min(cost_a,cost_b)=}")
    return dp[a+1][b+1]

print(recursive(-1,-1))
a,b = 0,0
for i in range(W):
    print(trace[a][b])
    if trace[a][b] == 1:
        a = i + 1
    else:
        b = i + 1