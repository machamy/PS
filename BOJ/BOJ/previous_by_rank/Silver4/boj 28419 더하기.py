import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = [*map(int, input().split())]
    even = sum(arr[1::2])
    odd = sum(arr[0::2])
    
    if N == 3:
        if even < odd:
            return -1
        else:
            return even - odd
    return abs(even - odd)
    
    

print(solve())  