import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def solve():
    N = int(input())
    arr = [0 for _ in range(10)]
    a = 1
    b = N
    def count(n,m):
        while n>0:
            arr[n%10] += m
            n //= 10

    current = 1
    while a <= b:
        while b % 10 != 9:
            count(b, current)
            b -= 1
        if b < a:
            break

        while a % 10 != 0:
            count(a, current)
            a += 1
        a //= 10
        b //= 10
        for i in range(10):
            arr[i] += (b-a+1) * current
        current *= 10

    print(*arr)

solve()