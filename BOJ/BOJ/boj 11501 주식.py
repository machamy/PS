import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    money = 0 
    Max = 0
    for i in range(len(A)-1, -1, -1):
        if A[i] > Max:
            maxPrice = A[i]
        else: 
            money += maxPrice - A[i]

    print(money)