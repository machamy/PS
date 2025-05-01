N,M = map(int,input().split())
if M < N:
    N,M = M,N
# 두수끼리 곱했을때 제곱수인경우의 수
MAX = M*N

# 1~M 중에서 소수를 찾는다.
prime_table = [True for _ in range(M+1)]
for i in range(4,M+1,2):
    prime_table[i] = False
for i in range(3,M+1):
    if prime_table[i] == True:
        for j in range(i+i,M+1,i):
            prime_table[j] = False

primes = [2] + [i for i in range(3,M+1,2) if prime_table[i]]
ans = 0
def get_mul_primes(n):
    res = 1
    for prime in primes:
        # print("get P ",n,prime)
        if prime > n:
            break
        if n % prime == 0:
            cnt = 1
            n //= prime
            while n % prime == 0:
                cnt += 1
                n //= prime
            if cnt % 2 == 0:
                res *= 1
            else:
                res *= prime
           

    return res
for A in range(1,N+1):
    m = get_mul_primes(A)
    add =int((M/m)**0.5)
    # print(A,m,add)
    ans += add

print(ans)