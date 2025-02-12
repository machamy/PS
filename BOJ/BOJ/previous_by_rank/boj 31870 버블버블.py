N = int(input())
arr = [*map(int, input().split())]

def bubblsort(arr):
    arr = arr[:]
    cnt = 0
    for i in range(N):
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt += 1
    return cnt

def reversebubble(arr):
    arr = arr[:]
    cnt = 0
    for i in range(N):
        for j in range(N-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt += 1
    return cnt

print(min(bubblsort(arr), reversebubble(arr)+1))