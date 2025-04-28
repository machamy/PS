import sys

input = sys.stdin.readline

N,A,B = map(int,input().split())

costs = [[*map(int,input().split())] for _ in range(N)]
costs.sort(key = lambda x : x[0] - x[1])

ans = 0
for i in range(A):
    ans += costs[i][0]
for j in range(A,N):
    ans += costs[j][1]

print(ans)

