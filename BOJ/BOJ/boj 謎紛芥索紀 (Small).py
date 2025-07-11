N = int(input())

ans = 0

for _ in range(N):
    C,K = map(int, input().split())
    ans += (K) * C

print(ans)