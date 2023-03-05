

def solve():
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    nums = set(arr)
    K = int(input())
    dp = [[0 for  _ in range(K)] for _ in range(N+1)]
    def fibo(n):
        if n == 0:
            return 1
        return n * fibo(n-1)

    q = fibo(len(nums))