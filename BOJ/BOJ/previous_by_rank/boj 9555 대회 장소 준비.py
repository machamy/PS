import sys

input = sys.stdin.readline

def solve():
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ok = [False for _ in range(102)]
    ok[-1] = True
    cnt = 0
    for i in range(N):
        for j in range(M):
            t1 = arr[i][j]
            if ok[t1]:
                continue
            for di,dj in [(0,1),(1,0),(1,1),(1,-1)]:
                ni,nj = (i + di, j + dj)
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                t2 = arr[ni][nj]
                if t1 == t2:
                    ok[t1] = True
                    cnt += 1
                    break
    
    print(cnt)

T = int(input())
for _ in range(T):
    solve()