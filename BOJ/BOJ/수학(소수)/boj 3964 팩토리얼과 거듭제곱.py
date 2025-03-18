import sys

input = sys.stdin.readline

MAX_K = 1_000_000_000_000
SQRT_MAX_K = int(MAX_K**0.5 + 1)
filter = [True] * (SQRT_MAX_K)
primes = []
# print(SQRT_MAX_K)
for i in range(2,SQRT_MAX_K):
    if filter[i] == False:
        continue
    primes.append(i)
    j = i + i
    while j < SQRT_MAX_K:
        filter[j] = False
        j += i
def solve():
    N,K = map(int,input().split())
    factors = {}
    for p in primes:
        # print(K)
        cnt = 0
        while K % p == 0:
            K //= p
            cnt += 1
        if cnt:
            factors[p] = cnt
            if K == 1:
                break
    else:
        factors[K] = 1
    ans = float('inf')
    print(factors)
    for f in factors:
        cnt = 0
        n = 1
        # 1 2 3 4 5 6 7 8 ... N
        while N >= f ** n:
            cnt += N // (f ** n) # 해당 소인수를 가지는지 확인 (2 : 2개 4: 1개 -> 2: 3개)
            n += 1
        print(cnt//factors[f])
        ans = min(ans,cnt//factors[f]) # N의 소인수개수 // K의 소인수 개수
    print(ans)

for _ in range(int(input())):
    solve()