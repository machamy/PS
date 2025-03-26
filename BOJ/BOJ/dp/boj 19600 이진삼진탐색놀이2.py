import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

def binary_search(A, value, left, right):
    # left, right = 0, n - 1
    cnt = 0
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == value:
            return cnt
        elif value < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
        cnt += 1
    return cnt

def ternary_search(A, value, left,right):
    # left, right = 0, n - 1
    cnt = 0
    while left <= right:
        left_third = left + (right - left) // 3
        right_third = right - (right - left) // 3
        if A[left_third] == value:
            return cnt
        elif A[right_third] == value:
            return cnt + 1
        cnt += 2
        if value < A[left_third]:
            right = left_third - 1
        elif value < A[right_third]:
            left = left_third + 1
            right = right_third - 1
        else:
            left = right_third + 1
    return cnt

MAX = 5001
A = list(range(MAX))
B_dict = [None] * MAX
T_dict = [None] * MAX
for e in range(int(input())):
    n,s,e = map(int,input().split())
    if B_dict[n] is None:
        B = T = 0
        tmp_B = [0 for _ in range(n+1)]
        tmp_T = [0 for _ in range(n+1)]
        for i in range(0,n):
            b = binary_search(A,A[i],0,n-1)
            t = ternary_search(A,A[i],0,n-1)
            B += b
            T += t
            tmp_B[i] = B
            tmp_T[i] = T
        B_dict[n] = tmp_B
        T_dict[n] = tmp_T
    
    B = B_dict[n][e] - B_dict[n][s-1]
    T = T_dict[n][e] - T_dict[n][s-1]
    
    # print(B_dict[n])
    # print(B,T)
    sys.stdout.write(str(T - B) + '\n')