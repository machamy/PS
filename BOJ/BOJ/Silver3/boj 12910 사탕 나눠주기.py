

def solve():
    N = int(input())
    brands = list(map(int, input().split()))

    brandcnt = [0] * 51
    for brand in brands:
        brandcnt[brand] += 1
    if brandcnt[1] == 0:
        print(0)
        return

    ans = 0 # 1~N까지 고르는 경우의 수의 합 brand[1]C1 * brand[2]C1 * ... * brand[N-1]C1
    current = 1 # 1~N-1까지 고르는 경우의 수
    for i in range(1,N+1):
        if brandcnt[i] == 0:
            break
        ans += current * brandcnt[i]
        current *= brandcnt[i]

    print(ans)

solve()