import sys

input = sys.stdin.readline 


primes = []
prime_chk =  [True] * 1_000_001

for i in range(2, 1_000_001):
    if prime_chk[i]:
        primes.append(i)
        for j in range(i * 2, 1_000_001, i):
            prime_chk[j] = False
for i in range(2, 1_000_001):
    if prime_chk[i]:
        primes.append(i)

def solve():
    S = int(input())
    for p in primes:
       if S % p == 0:
           # p가 소인수임
           if p <= 1_000_000:
               print("NO")
               return
    print("YES")

for _ in range(int(input())):
    solve()