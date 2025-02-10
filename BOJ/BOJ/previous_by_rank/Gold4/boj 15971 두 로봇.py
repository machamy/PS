import sys, heapq

input = sys.stdin.readline


MAX = 1_000_000_001


def solve():
    N, a, b = map(int, input().split())
    matrix = [[] for _ in range(N + 1)]
    if a == b:
        print(0)
        return

    for _ in range(N - 1):
        x, y, c = map(int, input().split())
        matrix[x].append((y, c))
        matrix[y].append((x, c))

    dists = [MAX] * (N + 1)
    dists[a] = 0
    q = [(dists[a], a, 0)]
    while q:
        c, e, max_len = heapq.heappop(q)
        # print("pop", e, c, max_len)
        if e == b:
            # print("end ", e, c, max_len)
            print(c - max_len)
            return
        if dists[e] < c:
            continue

        for data in matrix[e]:
            nxt, cost = data
            nxt_dist = c + cost
            if nxt_dist < dists[nxt]:
                dists[nxt] = nxt_dist
                heapq.heappush(q, (nxt_dist, nxt, max(max_len, cost)))


solve()
