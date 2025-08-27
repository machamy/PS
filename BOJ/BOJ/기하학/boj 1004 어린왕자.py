import sys

input = sys.stdin.readline

def is_in(x,y,circle):
    if (x - circle[0]) ** 2 + (y - circle[1]) ** 2 <= circle[2] ** 2:
        return True
    return False

def check(x,y,circles):
    res = []
    for i,c in enumerate(circles):
        if is_in(x,y,c):
            res.append(i)
    return res

def solve():
    a,b,x,y = map(int,input().split())
    n = int(input())
    circles = [list(map(int,input().split())) for _ in range(n)]
    A = check(a,b,circles)
    B = check(x,y,circles)

    # print(A)
    # print(B)
    result = set(A) ^ set(B)
    # print(result)
    print(len(result))

for _ in range(int(input())):
    solve()