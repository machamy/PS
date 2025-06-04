import sys

input = sys.stdin.readline

def quick_sort(arr, low, high):
    stack = []
    stack.append((low, high))
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = partition(arr, low, high)
            stack.append((low, pivot - 1))
            stack.append((pivot + 1, high))

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def solve():
    N,Q = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(A)

    sums = [0] * (N+1)
    for i in range(1, N+1):
        sums[i] = sums[i-1] + B[i-1]
    

    for i in range(Q):
        L,R = map(int, input().split())
        ans = sums[R] - sums[L-1]
        print(ans)

solve()