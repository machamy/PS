import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

nums = [-1 for _ in range(N+1)] # 파이썬 dict은 순서가 있던가? 
num_to_id = dict() #
graph_by_id = [list() for _ in range(N+1)]

for i in range(1,N+1):
    n = int(input(),2)
    num_to_id[n] = i
    nums[i] = n

for i in range(1,N+1):
    n = nums[i]
    for j in range(K):
        bit = 1 << j
        nxt = n ^ bit
        if nxt in num_to_id:
            nxt_id = num_to_id[nxt]
            graph_by_id[i].append(nxt_id)

q = deque()
q.append(1)
path = [-1 for _ in range(N+1)]
while q:
    id = q.popleft()
    for nxt_id in graph_by_id[id]:
        if path[nxt_id] == -1: # visited == False 임.
            path[nxt_id] = id # 이전값 저장, 거꾸로 추적하기 위함.
            q.append(nxt_id)

M = int(input())
for _ in range(M):
    id = int(input())
    if path[id] == -1:
        print(-1)
        continue
    ans = []
    while id != 1:
        ans.append(id)
        id = path[id]
    ans.append(1)
    print(*ans[::-1])