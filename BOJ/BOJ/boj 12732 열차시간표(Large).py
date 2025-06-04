import sys
import heapq

input = sys.stdin.readline


def find(arr, a):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m][0] < a:
            l = m + 1
        else:
            r = m
    return l

def parse_time(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def solve():
    T = int(input())
    NA, NB = map(int, input().split())
    A2B = []
    B2A = []
    
    for _ in range(NA):
        a,b = input().split()
        A2B.append((parse_time(a), parse_time(b)))
    for _ in range(NB):
        a,b = input().split()
        B2A.append((parse_time(a), parse_time(b)))
    
    A2B.sort(key=lambda x: x[1])
    B2A.sort(key=lambda x: x[1])
    cnt_A = NA
    cnt_B = NB
    heap_A = list(A2B)
    heap_B = list(B2A)
    heapq.heapify(heap_A)
    heapq.heapify(heap_B)

    for a, b in A2B:
        while heap_B and heap_B[0][0] < b + T:
            heapq.heappop(heap_B)
        if heap_B:
            cnt_B -= 1
            heapq.heappop(heap_B)
    
    for a, b in B2A:
        while heap_A and heap_A[0][0] < b + T:
            heapq.heappop(heap_A)
        if heap_A:
            cnt_A -= 1
            heapq.heappop(heap_A)



    return cnt_A, cnt_B

for i in range(int(input())):
    res = solve()
    print(f"Case #{i + 1}: {res[0]} {res[1]}")