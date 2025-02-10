import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    heights = [*map(int, input().split())]

    result = [0 for _ in range(n)]
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] < heights[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1] + 1
        stack.append(i)

    print(*result)


solve()
