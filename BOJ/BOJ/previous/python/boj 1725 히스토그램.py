import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = [int(input()) for _ in range(N)]

    s = [0]
    ans = 0

    for i in range(1,N):
        while s and arr[s[-1]] >= arr[i]:
            w = i - s[-1]
            h = min(arr[s.pop()],arr[i])
            ans = max(h * w,ans)
        s.append(i)

    while s:
        h = arr[s.pop()]
        w = N - 1 - s[-1] if s else size
        ans = max(ans,h*w)




solve()