
# 점수의 수, 태수의 새로운 점수, 랭킹 점수의 수 
N, TS, P = map(int, input().split())
p = min(P,N)
if N == 0:
    print(1)
    exit()
# 점수 리스트
scores = list(map(int, input().split()))

ans = -1
for i in range(p):
    if TS >= scores[i]:
        ans = i + 1
        break


if N >= P and scores[p-1] == TS:
    ans = -1

if ans == -1 and N < P:
    ans = N+1
print(ans)