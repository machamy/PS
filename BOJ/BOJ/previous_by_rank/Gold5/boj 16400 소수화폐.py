import sys
input = sys.stdin.readline

MOD = 123_456_789

N = int(input())

prime_arr = [True] * (N+1)
prime_arr[0] = False
primes = set(i for i in range(1,N+1))

for i in range(2,int(N ** 0.5)+1):
    if not prime_arr[i]:
        continue
    n = i + i
    while n <= N:
        if prime_arr[n]:
            primes.remove(n)
        prime_arr[n] = False
        n += i

dp = [0 for _ in range(N+1)]
dp[0] = 1
for p in primes:
    for i in range(2,N+1):
        if i - p < 0:
            continue
        dp[i] = (dp[i] + dp[i-p]) % MOD
# print([i for i in range(N+1)])
# print(dp)
print(dp[N])




#solve()