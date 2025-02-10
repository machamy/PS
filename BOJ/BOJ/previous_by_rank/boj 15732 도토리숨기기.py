import sys

input = sys.stdin.readline
def solve():
    N,K,D = map(int, input().split())
    rules = [list(map(int, input().split())) for _ in range(K)]

    def dotori(idx):
        res = 0
        for A,B,C in rules:
            if A <= idx:
                res += (min(B,idx) - A) // C + 1
        return res
    
    # lower bound
    left_idx = 0
    right_idx = N
    while left_idx < right_idx:
        mid = (left_idx + right_idx) // 2

        n = dotori(mid)
        if n < D:
            left_idx = mid + 1
        else:
            right_idx = mid
    print(left_idx)


solve()