import sys

def solve():
    n = int(input())
    arr = [input() for _ in range(n)]

    result = list(arr[0])
    for i in range(len(arr[0])):
        if any(arr[j][i] != arr[0][i] for j in range(1, len(arr))):
            result[i] = "?"

    print(*result,sep="")

solve()