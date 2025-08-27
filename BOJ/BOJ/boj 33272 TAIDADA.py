
N,M,K = map(int,input().split())

"""
3 5 2

1 2 3 4 5
001
010
011
100
101

2
010

"""

A = [None for _ in range(N)]
cnt = 0
used = set()
for i in range(1,M+1):
    if i in used:
        continue
    A[cnt] = i
    cnt += 1
    other = i ^ K
    if other <= M:
        used.add(other)

    if cnt == N:
        break

if cnt < N:
    print(-1)
else:
    print(*A[:cnt])