import sys


# 첫 수는 무조건 +
# 두번째 수는 무조건 -
# 나머지는 +,- 둘다 가능
# arr[0] - arr[1] 은 고정값
# arr[2:] 에서 +와 -를 취사 선택
# 따라서, (arr[0] - arr[1]) - arr[2:]에서 취사선택한 합 = T
# arr[2:]에서 취사선택한 합 = (arr[0] - arr[1]) - T
# arr[2:]에서 취사선택한 합 = X
# 각 i에 대하여,
# 오른쪽부터 확인후 미리 빼주기 (두번 빼면 +임) <<< 틀림... Plus끼리 붙어있으면 문제생김
"""
5 4
12 10 4 3 5
"""
# 오른쪽부터 확인하면서, 더하는 경우엔 2 저장
# 빼는 경우엔 1 저장
# 전체 출력

MINUS = 1
PLUS = 2

def sovle():
    N,T = map(int,sys.stdin.readline().split())
    arr = list(map(int,sys.stdin.readline().split()))
    
    if N == 1:
        return
    if N == 2:
        print(1)
        return
    #offset = min(T,sum(arr[:2]))
    offset = 10000 # 100 * 100 = 10000
    _range = 2 * offset + 1
    dp = [[0 for _ in range(_range)] for _ in range(N+1)]
    
    dp[1][arr[0]-arr[1] + offset] = MINUS
    for i in range(2,N):
        for j in range(_range):
            if dp[i-1][j] == 0:
                continue
            if j + arr[i] < _range:
                dp[i][j+arr[i]] = PLUS
            if j - arr[i] >= 0:
                dp[i][j-arr[i]] = MINUS
    
    current = T + offset
    minus_cnt = 0
    
    ans = [0 for _ in range(N)]
    for i in range(N-1,1,-1):
        # print("c : ",current- offset)
        # print("i : ",i,dp[i][current])
        if dp[i][current] == PLUS:
            ans[i] = 2
            current -= arr[i]
        else:
            ans[i] = 1
            current += arr[i]
            minus_cnt += 1

    for i in range(2,N):
        print(ans[i])
    print(1)

sovle()

