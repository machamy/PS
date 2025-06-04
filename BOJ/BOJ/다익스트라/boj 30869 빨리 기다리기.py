import sys
import heapq

input = sys.stdin.readline

N,M,K = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,cost,g = map(int, input().split())
    adj[s].append((e,cost,g))

dists = [[float('inf') for _ in range(K+1)] for _ in range(N+1)]
q = [[] for _ in range(K+1)]
q[K] = [(0,1)] # (시간, 위치, 남은 빨리 기다리기)
"""
3 3 1
1 3 7 2
1 2 2 5
2 3 4 4

1 ->
"""
for k in range(K,0,-1):
    while q[k]:
        time, pos = heapq.heappop(q[k])
        # print(f"pos: {pos}, wait: {k}, time: {time}")
        if dists[pos][k] < time:
            continue
        for nxt, cost, interval in adj[pos]:
            a,b = divmod(time, interval) 
            nxt_time = 0
            if b == 0:
                nxt_time = cost + interval * a
            else:
                nxt_time = cost + interval * (a+1)
                if time + cost < dists[nxt][k-1]:
                    dists[nxt][k-1] = time + cost
                    heapq.heappush(q[k-1], (time+cost, nxt))
            if nxt_time < dists[nxt][k]:
                dists[nxt][k] = nxt_time
                heapq.heappush(q[k], (nxt_time, nxt))
                # print(f"push: {nxt_time}, {nxt}, {wait}")
while q[0]:
    time, pos = heapq.heappop(q[0])
    if dists[pos][0] < time:
        continue
    for nxt, cost, interval in adj[pos]:
        a,b = divmod(time, interval) 
        nxt_time = 0
        if b == 0:
            nxt_time = cost + interval * a
        else:
            nxt_time = cost + interval * (a+1)
        if nxt_time < dists[nxt][0]:
            dists[nxt][0] = nxt_time
            heapq.heappush(q[0], (nxt_time, nxt))
# for i in range(K, -1, -1):
#     print(f"--- k {i} ---")
#     for j in range(0, N+1):
#         print(dists[j][i], end=' ')
#     print()
res = min(dists[N])
if res == float('inf'):
    print(-1)
else:
    print(res)

