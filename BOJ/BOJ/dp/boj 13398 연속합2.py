N = int(input())
dp = [[float("-inf"),float("-inf")] for _ in range(N+1)]
arr = list(map(int,input().split()))
ans = float("-inf")
if N == 1:
    print(arr[0])
    exit()
for tmp_i,e in enumerate(arr):
    i = tmp_i + 1
    if i == 1:
        dp[1][0] = e
        dp[1][1] = e
        continue
    dp[i][0] = max(dp[i-1][0]+e,e) # 이전연속합 + 자기자신 VS 자기자신(앞에서 끊기)
    dp[i][1] = max(dp[i-1][1]+e,dp[i-1][0]) # 이전연속합 + 자기자신 VS 새로 끊어보기
    ans = max(ans,max(dp[i]))
# print(dp)
print(ans)