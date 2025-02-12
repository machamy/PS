import sys
from collections import deque

input = sys.stdin.readline


def solve():
    # n : 도시의 개수
    # m : 도로의 개수
    n, m = map(int, input().split())

    # 초기 도시 상태
    cities = [tuple(map(int, input().split())) for _ in range(m)]
    # 앞의로의 계획
    queue = [tuple(map(int, input().split())) for _ in range(int(input()))]

    # 길 초기화
    roads = [set() for _ in range(n)]
    for a, b in cities:
        roads[a - 1].add(b - 1)
        roads[b - 1].add(a - 1)

    # 최소 거리 초기화
    def bfs(visit, distances):
        q = deque([0])
        visit[0] = True

        while q:
            e = q.popleft()

            for nxt in roads[e]:
                if visit[nxt]:
                    continue
                visit[nxt] = True
                q.append(nxt)
                distances[nxt] = distances[e] + 1

    visit = [False for _ in range(n)]
    distances = [0 for _ in range(n)]
    bfs(visit, distances)

    # 도로 계힉 시작
    for cmd, a, b in queue:
        a -= 1
        b -= 1

        if cmd == 1:
            roads[a].add(b)
            roads[b].add(a)
        elif cmd == 2:
            roads[a].remove(b)
            roads[b].remove(a)

        visit = [False for _ in range(n)]
        bfs(visit, distances)

        for i in range(n):
            if not visit[i]:
                distances[i] = -1
        print(*distances)
        pass


if __name__ == "__main__":
    solve()
