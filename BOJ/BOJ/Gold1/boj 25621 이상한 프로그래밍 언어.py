import sys

input = sys.stdin.readline

MOD = 1_000_000_007
LARGE = 1_000_000_000

PLUS = "+"
SUB = "-"
MUL = "*"

"""
기본 아이디어 : 각 두 연산에 대해 최대가 되는 값을 구한다

각 연산 입력의 최대값은 10^9


특이 케이스 
- *0 이 있는경우
- 뺄셈으로 수가 엄청 작아지는 경우
"""


def solve(N, K):

    parser = lambda x: (x[0], int(x[1:]))

    ans = K
    is_small = True
    for i in range(N):
        a, b = sorted(map(parser, input().split()))  # ['*', '+', '-']

        if a[0] == b[0]:
            # 두 연산이 같은 경우
            if a[0] == SUB:
                ans -= a[1]
                if not is_small and ans < 0:
                    ans += MOD
            elif a[0] == PLUS:
                ans += b[1]
            else:
                ans *= b[1]
                if ans == 0:
                    is_small = True
        else:
            # 두 연산이 다른경우
            if b[0] == SUB:
                # 뺄셈이라면 다른 연산을 선택
                if a[0] == MUL:  # *-
                    if a[1] == 0:
                        ans -= b[1]
                        if not is_small and ans < 0:
                            ans += MOD
                    else:
                        ans *= a[1]
                else:  # +-
                    ans += a[1]
            else:  # a[0] == MUL and b[0] == PLUS *+
                # 곱셈이라면 크기를 비교
                if a[1] < 2:
                    # 0또는 1을 곱한다면 +에 비해 손해.
                    ans += b[1]
                elif not is_small:
                    # 10^9보다 크다면 곱하는게 이득!
                    ans *= a[1]
                else:
                    # 아니라면 크기 비교를 해야함
                    ans = max(ans * a[1], ans + b[1])
        # print(is_small, ans)

        if ans < 0:
            ans = 0

        if not is_small:
            ans %= MOD
        elif ans >= (N - i) * LARGE:
            is_small = False
            ans %= MOD

    print(ans % MOD)


N, K = map(int, input().split())
solve(N, K)
