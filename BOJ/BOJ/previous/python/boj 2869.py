import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def solve():
    A, B, V = map(int, input().split())

    if V < A:
        print(1)
        return
    V -= A
    if V / (A - B) != (V // (A - B)):
        print((V // (A - B) + 2))
    else:
        print((V // (A - B) + 1))


solve()
