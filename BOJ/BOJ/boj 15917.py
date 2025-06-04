import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue
    while n % 2 == 0:
        n //= 2
        if n == 1:
            print(1)
            break
    else:
        print(0)