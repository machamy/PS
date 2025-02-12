import sys
from collections import deque

input = sys.stdin.readline

# 사람, 서점 수
N,M = map(int,input().split())
wishes = list(map(int,input().split()))
books = list(map(int,input().split()))
C = [list(map(int,input().split())) for _ in range(M)]

# 0 소스
# 1~100 사람
# 101~200 서점
# 201 싱크

capacity = [[0 for _ in range(202)] for _ in range(202)]
flow = [[0 for _ in range(202)] for _ in range(202)]
adj = [[] for _ in range(202)]

for i in range(N):
    # 소스 - 사람 연결
    capacity[0][i+1] = wishes[i]
    adj[0].append(i+1)
    adj[i+1].append(0)
    for j in range(M):
        # 사람 - 서점 연결
        capacity[i+1][100+j+1] = C[j][i]
        adj[i+1].append(100+j+1)
        adj[100+j+1].append(i+1)

for i in range(M):
    # 서점 - 싱크 연결
    capacity[100+i+1][201] = books[i]
    adj[100+i+1].append(201)
    adj[201].append(100+i+1)

def max_flow(S,E):
    # 최대 유량 알고리즘으로 풀기
    ans = 0
    while True:
        # 증가경로가 생기지 않을 때까지 반복
        q = deque()
        q.append(S)
        visited = [-1 for _ in range(202)]
        while q:
            current = q.popleft()
            for nxt in adj[current]:
                if capacity[current][nxt] - flow[current][nxt] > 0 and visited[nxt] == -1:
                    q.append(nxt)
                    visited[nxt] = current

                    if nxt == E:
                        # sink 도달
                        break
        
        if visited[E] == -1:
            # 증가 경로가 없으면 종료
            break

        m = float('inf')
        s,e = S,E
        # print(f"{e} <- ",end="")
        while e != s:
            m = min(m,capacity[visited[e]][e] - flow[visited[e]][e])
            e = visited[e]
            # print(f"{e} <-({capacity[visited[e]][e]}-{flow[visited[e]][e]}) ",end="")
        s,e = S,E
        while s != e:
            flow[visited[e]][e] += m
            flow[e][visited[e]] -= m
            e = visited[e]
        ans += m
        # print("add",m)

    return ans
# print(adj[0])
# print(adj[1])
print(max_flow(0,201))