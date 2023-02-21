import sys

input = sys.stdin.readline

MAX = 2_000_000


def solve():
    N = int(input())
    schools = [*map(int, input().split())]

    arr = [0 for _ in range(MAX + 2)]
    ans = 0
    for num in schools:
        arr[num] += 1

    for i in range(1, MAX + 1):
        cnt = 0
        for j in range(i, MAX + 1, i):
            cnt += arr[j]
        if 1 < cnt:
            ans = max(ans, cnt * i)

    print(ans)
    return


solve()
