import sys
input = sys.stdin.readline

print = sys.stdout.write

MAX = 1_000_000
is_prime = [True] * 1000001
is_prime[0] = is_prime[1] = False
for i in range(2, 1001):
    if is_prime[i]:
        for j in range(i*i, 1000001, i):
            is_prime[j] = False
prime_set = set()
for i in range(2, 1000001):
    if is_prime[i]:
        prime_set.add(i)            


N = int(input())
is_odd_prime = [False] * 1000001
odd_cnt = 0

for _ in range(N):
    nxt = int(input())
    
    # 나머지
    for p in prime_set:
        
        # 1인경우
        if nxt == 1:
            break
        # 소수인 경우
        if is_prime[nxt]:
            if is_odd_prime[nxt]:
                odd_cnt -= 1
                is_odd_prime[nxt] = False
            else:
                odd_cnt += 1
                is_odd_prime[nxt] = True
            break
        
        while nxt % p == 0:
            if is_odd_prime[p]:
                odd_cnt -= 1
            else:
                odd_cnt += 1
            is_odd_prime[p] = not is_odd_prime[p]
            nxt //= p
    if odd_cnt:
        print("NE\n")
    else:
        print("DA\n")
        
