import sys



def solve():
    N = int(input())
    data = list(map(int, input().split()) for _ in range(N))
    
    dp = [0 for _ in range(N+1)] # dp[1] : 1일까지 일했을 때의 최대 수익

    # 1일부터 시작
    for i in range(1,N+1):
        
        t,p = data[i-1] # 해당 날짜의 필요 날짜, 수익
        end_of_work = i + t - 1 # 상담이 끝나는 날짜
        
        dp[i] = max(dp[i], dp[i-1]) # 이전 값 끌고오기
        if end_of_work > N:
            # 회사에 없을땐 상담 불가
            continue
        dp[end_of_work] = max(dp[end_of_work], dp[i-1] + p)
    print(dp[N])

solve()


