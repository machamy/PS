import math



"""
nCr = n!/((n-r)!r!)
5와 2의 개수를 셈


"""

def count_k(n,k):
    res = 0
    while(n >= k):
        res += n // k
        n //= k
    return res

N,M = map(int,input().split())

tw = count_k(N, 2) - count_k(M, 2) - count_k(N-M, 2)
fv = count_k(N, 5) - count_k(M, 5) - count_k(N-M, 5)
print(min(tw,fv))