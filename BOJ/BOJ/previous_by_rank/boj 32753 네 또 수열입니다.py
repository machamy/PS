
N,K = map(int, input().split())

if N == 1:
    print(*([1]*K), sep=' ')
elif N == 2 and K == 1:
    print("1 2")
else:
    print("-1")