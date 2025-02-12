import sys
import heapq as hq

input = sys.stdin.readline


def solve():
    N = int(input())
    arr = [*map(int, input().split())]
    M = int(input())
    cmds = [[*map(int, input().split())] for _ in range(M)]

    D = dict()
    pq = [(0, tuple(arr))]

    while pq:
        cost, state = hq.heappop(pq)
        if state in D:
            if cost < D[state]:
                D[state] = cost
            else:
                continue
        else:
            D[state] = cost

        for cmd in cmds:
            l, r, c = cmd
            arr = list(state)
            arr[l - 1], arr[r - 1] = arr[r - 1], arr[l - 1]
            hq.heappush(pq, (cost + c, tuple(arr)))

    LAST_STATE = tuple(sorted(arr))
    if LAST_STATE in D:
        print(D[LAST_STATE])
    else:
        print(-1)


solve()
