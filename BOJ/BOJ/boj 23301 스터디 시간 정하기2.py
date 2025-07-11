import sys

input = sys.stdin.readline

def main():
    N,T = map(int,input().split())
    arr = [0 for _ in range(1001)] 
    for _ in range(N):
        K = int(input())
        for _ in range(K):
            S,E = map(int,input().split())
            for t in range(S,E):
                arr[t] += 1
    
    prefix = [0 for _ in range(1002)]
    for i in range(1001):
        prefix[i] = prefix[i-1] + arr[i]
    ans = (-1,-1)
    MAX = 0
    # print(prefix)
    for i in range(T-1,1001):
        num = prefix[i] - prefix[i-T]
        # print(f"{prefix[i]=},{prefix[i-T]=},{num=}")
        if num > MAX:
            MAX = num
            ans = (i-T+1,i+1)
    print(*ans)

main()