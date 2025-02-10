import sys

input = sys.stdin.readline

MAX_K = 1_000_000_000_000

def solve():
    N,K = map(int, input().split())
    
    factors = {}
    for i in range(2, int(K**0.5)+1):
        cnt = 0
        while K % i == 0:
            K //= i
            cnt += 1
        if cnt:
            factors[i] = cnt
    factors[K] = 1
    
    ans = float('inf')
    for factor, factor_cnt in factors.items():
        cnt, depth, num = 0, 1, N
        print(f'factor: {factor}, factor_cnt: {factor_cnt}')
        while num > 1 and num < factor**depth:
            cnt += num // (factor**depth)
            depth += 1
        
        ans = min(ans, cnt // factor_cnt)
    print(ans)

for _ in range(int(input())):
    solve()