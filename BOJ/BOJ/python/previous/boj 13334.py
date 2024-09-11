import sys
from collections import deque, defaultdict
import heapq

input = sys.stdin.readline

def solve():
    N = int(input())
    houses = [sorted(map(int,input().split())) for _ in range(N)]
    houses.sort(key= lambda x:x[1])
    d = int(input())
    ans = 0
    hq = []
    for h in houses:
        if abs(h[0]-h[1]) > d:
            continue
        if not hq:
            heapq.heappush(hq, h)
        else:
            while hq[0][0] < h[1] - d:
                heapq.heappop(hq)
                if not hq:
                    break
            heapq.heappush(hq, h)
        ans = max(ans,len(hq))
    return ans


print(solve())