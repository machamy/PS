import sys

input=sys.stdin.readline

"""
등차수열의 합 : 공비(초항+마지막항)/2

N*2 == L * (초항+마지막항) ==  L * (2*초항 + (n-1) 공차) == L * (2*초항 + L - 1)
N = 초항*L + (L-1) * L // 2
초항 * L = (N - (L-1) * L // 2)
초항 * 2 == (N*2)/L - L + 1
여기서 L은 수열의 크기.
"""
def solve():
    N, L = map(int,input().split())

    for i in range(L,100):
        ad = (N - (i-1)*i/2)
        if ad % i != 0:
            continue

        a = ad//i
        if a >= 0:
            print(*(a+k for k in range(i)),end=" ")
            return

    print(-1)

solve()