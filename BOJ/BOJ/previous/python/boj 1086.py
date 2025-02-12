

def solve():
    N = int(input())
    strarr = [input() for _ in range(N)]
    arr = [int(s) for s in strarr]
    nums = set(arr)
    K = int(input())
    # dp[i][k] 는 i(비트)를 뽑아 만든 순열준 k의 나머지를 가진 순열의 개수
    dp = [[0 for  _ in range(K)] for _ in range(1<<(N+1))]
    dp[0][0] = 1
    mods =[10**i % K for i in range(51)]
    def gcd(a,b):
        if b == 0:
            return a
        return gcd(b,a%b)
    def fibo(n):
        if n == 0:
            return 1
        return n * fibo(n-1)
    for b in range(1<<N): # 경우의 수 전부 순환
        for i in range(N): # 다음에 켤 비트
            if b & (1<<i): # 중복이면 무시
                continue
            nxt_b = b|(1<<i)
            for j in range(K):
                remain = (j*mods[len(strarr[i])] % K + arr[i] % K) % K
                dp[nxt_b][remain] += dp[b][j]
    p = dp[(1<<N)-1][0]
    q = fibo(len(nums))
    r = gcd(p,q)
    p //= r
    q //= r
    print(f"{p}/{q}")

solve()