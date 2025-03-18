import sys;
input = sys.stdin.readline


def solve():

    N  = int(input())
    arr = [[0 for _ in range(N)] for _ in range(4)]
    for i in range(N):
        a,b,c,d = map(int,input().split())
        arr[0][i] = a
        arr[1][i] = b
        arr[2][i] = c
        arr[3][i] = d
    d0 = {}

    for a in arr[0]:
        for b in arr[1]:
            if a+b in d0:
                d0[a+b] += 1
            else:
                d0[a+b] = 1

    result = 0
    for c in arr[2]:
        for d in arr[3]:
            if -(c+d) in d0:
                result += d0[-(c+d)]
    print(result)

solve()