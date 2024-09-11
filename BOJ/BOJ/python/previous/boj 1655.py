import sys
import heapq as hq

input = sys.stdin.readline


def solve():
    MIN = []
    MAX = []
    N = int(input())
    MAX.append(-int(input()))
    print(-MAX[0])
    for _ in range(N-1):
        n = int(input())
        if len(MIN) < len(MAX):
            hq.heappush(MIN, n)
        else:
            hq.heappush(MAX, -n)

        if MIN[0] < -MAX[0]:
            m,M = hq.heappop(MIN),hq.heappop(MAX)
            hq.heappush(MIN,-M)
            hq.heappush(MAX,-m)
        print(-MAX[0])



solve()
