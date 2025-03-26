import sys
import bisect

input = sys.stdin.readline

def solve():
    N,K,T = map(int,input().split())
    QQ = list(map(int,input().split()))
    Q = []
    for i,e in enumerate(set(QQ)):
        Q.append(e%K)
    Q.sort()
    A = list(map(int,input().split()))
    # print(Q)
    current_sum = 0
    for a in A:
        current_sum += a
        current_sum %= K
        Max = K-current_sum - 1
        # print(f"{Max=}")
        i = bisect.bisect_left(Q,Max)
        if i == len(Q):
            i -= 1
        if Q[i] > Max:
            i -= 1
        # print(i,end=" ")
        print((Q[i]+current_sum)%K,end=" ")
    print()
    


solve()