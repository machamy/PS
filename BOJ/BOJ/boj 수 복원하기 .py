
MAX = 100_000

prime_table = [True] * (MAX + 1)
primees = []

for i in range(2, MAX + 1):
    if prime_table[i]:
        primees.append(i)
        for j in range(i * 2, MAX + 1, i):
            prime_table[j] = False


T = int(input())


def solve():
    N = int(input())

    # 소인수 분해하기. 개수도 저장
    factors = []
    for p in primees:
        if p * p > N:
            break
        if N % p == 0:
            count = 0
            while N % p == 0:
                count += 1
                N //= p
            factors.append((p, count))

    if N > 1:
        factors.append((N, 1))
    factors.sort()

    return factors



for _ in range(T):
    result = solve()
    if result:
        for p, c in result:
            print(p, c)