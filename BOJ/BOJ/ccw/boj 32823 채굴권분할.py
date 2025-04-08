import sys
import math

input = sys.stdin.readline

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


def is_cross(a, b, c, d):
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)
    if ab < 0 and cd < 0:
        return True
    # 선분 위의 있는 경우는 없음 
    # if ab == 0 and cd == 0:
    #     if a > b:
    #         a,b = b,a
    #     if c > d:
    #         c,d = d,c
    #     return c <= b and a <= d
    return False

def solve():
    N = int(input())
    lines = []
    for _ in range(N):
        a,b = map(int,input().split())
        line = []
        x = math.cos(math.radians(a/10)) * 1000
        y = math.sin(math.radians(a/10)) * 1000
        line.append((x,y))
        x = math.cos(math.radians(b/10)) * 1000
        y = math.sin(math.radians(b/10)) * 1000
        line.append((x,y))
        lines.append(line)
    pp = []
    for _ in range(2):
        degree,dist = map(int,input().split())
        x = math.cos(math.radians(degree/10)) * dist
        y = math.sin(math.radians(degree/10)) * dist
        pp.append((x,y))
    cnt = 0
    for i in range(N):
        line = lines[i]
        if is_cross(line[0],line[1],pp[0],pp[1]):
            cnt += 1
    # print(cnt)
    if cnt % 2 == 0:
        print("YES")
    else:
        print("NO")

solve()