N,K = map(int,input().split())
A = list(map(int,input().split()))

addictive = [0 for _ in range(N+1)]
"""
수열의 합 / 수열의 길이 = 평균
(N까지 합  - x까지 합) / (N - x) = 구간 평균

"""
sums_count = dict()
ans = 0
for i in range(N):
    addictive[i] = addictive[i-1] + A[i]
    required_sum = addictive[i] - (i+1) * K # 초과된 합
    if required_sum not in sums_count:
        sums_count[required_sum] = 0
    ans += sums_count[required_sum] # 기존 초과 합 있으면, 그걸 빼면 됨
    sums_count[required_sum] += 1
    # print(required_sum,sums_count)

if 0 in sums_count:
    ans += sums_count[0]
print(ans)