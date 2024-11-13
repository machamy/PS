import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = [*map(int,input().split())]

    idx = 0
    if N <= 2:
        if N == 1:
            return 'A'
        if N == 2:
            if arr[0] == arr[1]:
                return arr[0]
            else:
                return 'A'

    a = ((arr[2] - arr[1]) // (arr[1] - arr[0])) if (arr[1] - arr[0]) else 0
    b = arr[1] - arr[0] * a
    for idx in range(2,N):
        if arr[idx] != arr[idx-1]*a+b:
            return 'B'
    return arr[-1]*a+b



print(solve())