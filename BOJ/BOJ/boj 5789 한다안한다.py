import sys

input = sys.stdin.readline

def solve():
    n = input().rstrip()
    mid = len(n) // 2
    if n[mid - 1] == n[mid]:
        print("Do-it")
    else:
        print("Do-it-Not")

for _ in range(int(input())):
    solve()