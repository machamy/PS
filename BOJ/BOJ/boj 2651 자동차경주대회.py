from collections import deque
MAX_DISTANCE = int(input())
N = int(input())
Distances = list(map(int,input().split()))
positions = [0]
for i,e in enumerate(Distances):
    positions.append(positions[i]+e)
Times = list(map(int,input().split()))
Times.append(0)
dp = [float("inf") for _ in range(N+2)]
path = [float("inf") for _ in range(N+2)]
dp[0] = 0

for i in range(N+1):
    current_pos = positions[i]
    nxt_idx = i + 1
    while nxt_idx <= N + 1 and positions[nxt_idx] - current_pos <= MAX_DISTANCE:
        if dp[nxt_idx] > dp[i] + Times[nxt_idx-1]:
            dp[nxt_idx] = dp[i] + Times[nxt_idx-1]
            path[nxt_idx] = i

        nxt_idx += 1

print(dp[N+1])

if dp[N+1] == 0:
    print(0)
else:
    q = deque([N+1])
    while q[0] != 0:
        q.appendleft(path[q[0]])

    q.popleft()
    q.pop()
    print(len(q))
    print(*q)

    # print(dp)