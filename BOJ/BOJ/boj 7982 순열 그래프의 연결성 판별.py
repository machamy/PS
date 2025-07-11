import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    arr = list(map(int,input().split()))

    sets = []
    current_max = 0
    for i in range(N):
        if current_max == i:
            sets.append([])
        num = arr[i]
        current_max = max(current_max,num)
        sets[-1].append(i+1)
    
    print(len(sets))
    for s in sets:
        print(len(s), end=" ")
        print(*s)
solve()