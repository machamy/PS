import sys

input = sys.stdin.readline

N,M = map(int, input().split())

"""
6 7
1 3
2 2
3 1
4 3
5 5
6 2

7
"""
# ' 3 ' 2 ' 1 ' 3 ' 5 ' 2'
# 1 + 2 + 1 + 2 + 1
# 7


deteceted = [list(map(int, input().split())) for _ in range(N)]
deteceted.sort()
deteceted.append((0,0))

ans = 0
prev_cnt = 0
for i,data in enumerate(deteceted):
    diff = prev_cnt - data[1]
    if diff > 0:
        ans += diff
    prev_cnt = data[1]

print(ans)