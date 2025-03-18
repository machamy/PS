import sys

input = sys.stdin.readline
N,K,Q = map(int,input().split())
food = list(map(int,input().split()))
distance = list(map(int,input().split()))
arr = []
for i in range(N):
    arr.append([distance[i] ,food[i] + distance[i] * K])

arr.sort(key = lambda x : (x[0],-x[1]))
M = 0
for i in range(len(arr)):
    if arr[i][1] < M:
        arr[i][1] = M
    else:
        M = arr[i][1]
# print(arr)
def bi(n):
    l = 0
    r = len(arr)
    while l < r:
        m = (l+r) // 2
        if arr[m][0] <= n:
            l = m + 1
        else:
            r = m
    return l

for _ in range(Q):
    q = int(input())
    ans = bi(q) - 1
    if ans < 0:
        print(0)
    else:
        print(arr[ans][1])