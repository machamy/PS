N = int(input())
arr = list(map(int, input().split()))
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

def s(i,k):
    return prefix_sum[i + k - 1] - prefix_sum[i - 1]

"""

"""

ans_k = -1
ans_minSum = float('inf')


for k in range(1, N//2 + 1):
    sums = [[s(i,k), i, i + k - 1] for i in range(1, N - k + 2)]
    sums.sort()
    for i in range(len(sums)):
        for j in range(i + 1, len(sums)):
            if sums[i][2] < sums[j][1] or sums[j][2] < sums[i][1]:
                if abs(sums[i][0] - sums[j][0]) <= ans_minSum:
                    ans_minSum = abs(sums[i][0] - sums[j][0])
                    ans_k = k  
                break

print(ans_k)
print(ans_minSum)
