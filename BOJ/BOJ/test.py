import sys
from collections import deque
import heapq

input = sys.stdin.readline

T = int(input())

def solve():
    x,y = map(int,input().split())

    dist = abs(y - x)
    root = int(dist**0.5)
    square = root ** 2
    if dist <= 3:
        print(dist)
    elif dist == dist**0.5:
        print(root * 2 -1)
    elif dist < square + root:
        print(root * 2)
    else:
        print(root*2 + 1)

for _ in range(T):
    solve()