import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    promises = [list(map(int, input().split())) for _ in range(N)]
    promises.sort(key=lambda x: [x[0],-x[1]])

    cnt = [0 for _ in range(366)]

    for a,b in promises:
        for i in range(a, b + 1):
            cnt[i] += 1
    ans = 0
    width = 0
    height = 0
    for i in range(1, 366):
        if cnt[i] == 0:
            ans += width * height
            width = 0
            height = 0
        else:
            width += 1
            height = max(height, cnt[i])
    
    print(ans + width * height)
    


solve()