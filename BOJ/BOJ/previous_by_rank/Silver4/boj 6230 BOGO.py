import sys

# 입력
N, M = map(int, sys.stdin.readline().split())

high_quality = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)  # 내림차순 정렬
low_quality = sorted([int(sys.stdin.readline()) for _ in range(M)])  # 오름차순 정렬
# high_quality = reversed(high_quality)  # 내림차순 정렬을 오름차순 정렬로 바꿈
ans = 0
for high in high_quality:
    ans += 1 
    while low_quality and low_quality[-1] >= high:
        low_quality.pop()
    if low_quality:
        low_quality.pop()
        ans += 1
print(ans)