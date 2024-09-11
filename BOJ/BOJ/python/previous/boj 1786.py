import sys
from collections import defaultdict, deque


def solve():
    T = input().rstrip()
    P = input().rstrip()

    """
    A B C D A B D A B C D
    0 0 0 0 1 2 2 1 2 3 4
    
    A B D A B C A B D
    0 0 0 1 2 2 0 1 2 
    """
    k_arr = [0 for _ in range(len(P))]

    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = k_arr[j - 1]

        if P[i] == P[j]:
            j += 1
            k_arr[i] = j

    result = []

    ans = j = 0
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = k_arr[j - 1]

        if T[i] == P[j]:
            if j == len(P) - 1:
                result.append(i - len(P) + 2)
                ans += 1
                j = k_arr[j]
            else:
                j += 1

    print(ans)
    print(*result)

solve()
