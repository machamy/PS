import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    shops = [tuple(map(int, input().split())) for _ in range(N)]

    distance = float('inf')
    ans = None
    for s in shops:
        if (max_distance := max((s[0] - another[0]) ** 2 + (s[1] - another[1]) ** 2 for another in shops)) < distance:
            distance = max_distance
            ans = s

    print(*ans)


solve()
