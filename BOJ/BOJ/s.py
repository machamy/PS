N = int(input())
N = 1000 - N

res = 0
for e in [500,100,50,5,1]:
    print(N, e, N // e, N % e)
    res += N // e
    N %= e
print(res)