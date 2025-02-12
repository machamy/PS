import sys

input = sys.stdin.readline

"""
K : 참여자 수
C : 한 봉지에 들어있는 사탕의 수

적어도 한명은 사탕을 잃어버림.

사탕은 K * X개를 사야하나, 한명 이상이 잃어버리므로 K*X + 1개를 사야함.
ex:
K=10, C=5 -> 불가능
K=10, C=7 -> 가능(3봉지)
K=1337, C=23 -> 가능(872봉지)


CY - KX = 1

C * Y ≡ 1 (mod K)
"""


def solve():
    K, C = map(int, input().split())

    # K * n + 1 과 C의 최소 공배수가 없으면 불가능

    if K == 1:
        return 2
    if C == 1:
        if K + 1 > 10**9:
            return False
        return K + 1

    # 확장 유클리드 호제법... 이게 뭐임?
    def extended_gcd(a, b):
        r = 0
        s1, s2 = 1, 0
        s = 0
        t1, t2 = 0, 1
        t = 0
        while b != 0:
            q, r = divmod(a, b)  # 몫, 나머지; 나머지는 유클리드 호제법과 같음
            a, b = b, r  # 유클리드 호제법과 같음
            s = s1 - q * s2
            s1, s2 = s2, s
            t = t1 - q * t2
            t1, t2 = t2, t
        if t1 < 0:
            t1 = (t1 + K) % K
        if a != 1 or t1 > 10**9:
            return False

    return extended_gcd(K, C)


T = int(input())
for _ in range(T):
    if (ans := solve()) is False:
        print("IMPOSSIBLE")
    else:
        print(ans)
