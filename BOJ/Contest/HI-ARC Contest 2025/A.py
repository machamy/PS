import sys

S = int(input())

H = I = A = R = C = 0

mul2 = [0] * 101
mul3 = [0] * 1001
for i in range(0,11):
    for j in range(0,11):
        mul2[i*j] += 1
        for k in range(0,11):
            mul3[i*j*k] += 1

ans = 0
for i in range(0,101):
    if  0 <= i - S <= 1000:
        ans += (mul2[i] * mul3[i-S])

print(ans)