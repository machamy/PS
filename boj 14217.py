import sys

input = sys.stdin.readline



def solve():
    n = int(input())
    prnts = [i for i in range(n)]

    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        if find(prnts,a) != find(prnts,b):
           union(prnts, a, b)

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())

        print(int(find(prnts, a) == find(prnts, b)))

    #print(prnts)

T = int(input())
for i in range(T):
    print(f"Scenario {i + 1}:")
    solve()
    print()