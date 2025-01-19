import sys

N = int(input())
A,B = map(int,input().split())

def solve():
    #  i번째 자습일에 정독실, 소학습실, 휴게실, 요양시 만족도
    satisfaction_data = [list(map(int,input().split())) for _ in range(N)]

    # dp[a][b][idx][has_Relaxed]
    # a : 요양신청횟수
    # b : 자습한 횟수(B이상은 b로)
    # idx : 현재 날짜
    # has_Relaxed : 0,1 휴게실 사용 여부
    dp = [[[[0, 0] for _ in range(N+1)] for _ in range(B+1)] for _ in range(A+1)]

    current_max_a = 0
    current_max_b = 0
    for i in range(N):
        p,q,r,s = satisfaction_data[i]
        learn_satis = max(p,q)
        for a in range(current_max_a + 1):
            for b in range(current_max_b + 1):
                study = max(dp[a][b][i][0], dp[a][b][i][1]) + learn_satis

                # 그냥 학습하기
                if b < B : 
                    dp[a][b+1][i+1][0] = max(dp[a][b+1][i+1][0], study)
                    current_max_b = max(current_max_b, b + 1)
                else:
                    dp[a][B][i+1][0] = max(dp[a][B][i+1][0], study)
                # 요양하기
                if a < A:
                    dp[a+1][b][i+1][0] = max(dp[a+1][b][i+1][0], max(dp[a][b][i]) + s)
                    current_max_a = max(current_max_a, a+1)
                # 휴게실 가기
                if dp[a][b][i][0] > 0:
                    dp[a][b][i+1][1] = dp[a][b][i][0] + r

    for a in range(A+1):
        for b in range(B+1):
            for f in (0,1):
                print(f"a:{a}, b:{b}, f:{f}")
                for i in range(N+1):
                    print(dp[a][b][i][f],end=' ')
                print()
            print()
        print()

    ans = 0
    for a in range(A+1):
        ans = max(ans, dp[a][B][N][0],dp[a][B][N][1])
    print(ans)

solve()