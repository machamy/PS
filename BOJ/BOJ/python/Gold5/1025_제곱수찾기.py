from math import sqrt;

N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
ans = -1
for i in range(N):
    for j in range(M):# 시작점
        for di in range(-N,N):
            for dj in range(-M,M):# 등차
                print(di,dj)
                num = 0
                a,b = i,j
                while 0 <= a < N and 0 <= b < M:
                    num = num * 10 + arr[a][b]
                    if di == 0 and dj == 0 : # 등차가 모두 0이면 -> 움직이지 않음
                        break
                    if int(sqr := sqrt(num)) == sqr:
                        ans = max(num,ans)
                    a += di
                    b += dj
print(ans)
                    