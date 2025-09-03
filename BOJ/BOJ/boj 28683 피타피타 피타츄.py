

# 직각삼각형이 포함해야하는 변의 길이의 제곱
N = int(input())
sqrtN = int(N ** 0.5)
ans = 0
ans_set = set()

if N == sqrtN * sqrtN:
    print(-1)
    exit()

# sqrtN이 대각선일때의 경우의 수 구하기.
for a in range(1, sqrtN + 1):
    b2 = N - a * a
    b = b2 ** 0.5
    if b == int(b):
        # ans += 1
        if a > b:
            ans_set.add((b, a, -1))
        else:
            ans_set.add((a, b, -1))


# sqrtN이 직선일때의 경우의 수 구하기.
# N + a^2 = c^2
# N = c^2 - a^2
# N = (c - a)(c + a)
factors = []
for i in range(1, sqrtN + 1):
    if N % i == 0:
        factors.append((i, N // i))

for a, b in factors:
    if a % 2 == b % 2:
        if a > b:
            a, b = b, a
        # ans += 1
        ans_set.add((-1, a, b))
 


# print(ans)
print(len(ans_set))