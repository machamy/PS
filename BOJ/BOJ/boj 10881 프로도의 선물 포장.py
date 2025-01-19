import sys

input = sys.stdin.readline
T = int(input())


def line_size(a,b,c):
    width = a[0] + b[0] + c[0]
    height = max(a[1], b[1], c[1])
    return width * height

def stack_size(a,b,c):
    # print(f"a: {a}, b: {b}, c: {c}")
    width = max(a[0], b[0]+c[0])
    height = a[1] + max(b[1],c[1])
    # print(f"width: {width}, height: {height}")
    # print(f"stack_size: {width * height}")
    return width * height

def solve():
    data = [list(map(int, input().split())) for _ in range(3)]
    a,b,c = data #정방향
    x,y,z = a[::-1], b[::-1], c[::-1] #90도 회전

    ans = 100_001_000
    # 1. 일렬로 3개
    ans = min(ans
              , line_size(a,b,c)
              , line_size(x,b,c)
              , line_size(a,y,c)
              , line_size(a,b,z)
              , line_size(x,y,c)
              , line_size(x,b,z)
              , line_size(a,y,z)
              , line_size(x,y,z)
            )
    # 2. 두개 + 위에 한개
    ans = min(ans
              , stack_size(a,b,c)
              , stack_size(x,b,c)
              , stack_size(a,y,c)
              , stack_size(a,b,z)
              , stack_size(x,y,c)
              , stack_size(x,b,z)
              , stack_size(a,y,z)
              , stack_size(x,y,z)
    )
    # print(f"ans2-1: {ans}")
    ans = min(ans
                , stack_size(b,a,c)
                , stack_size(y,a,c)
                , stack_size(b,x,c)
                , stack_size(b,a,z)
                , stack_size(y,x,c)
                , stack_size(y,a,z)
                , stack_size(b,x,z)
                , stack_size(y,x,z)
        )
    # print(f"ans2-2: {ans}")
    ans = min(ans
            , stack_size(c,a,b)
            , stack_size(z,a,b)
            , stack_size(c,x,b)
            , stack_size(c,a,y)
            , stack_size(z,x,b)
            , stack_size(z,a,y)
            , stack_size(c,x,y)
            , stack_size(z,x,y)
              )
    # print(f"ans2-3: {ans}")

    print(ans)

for _ in range(T):
    solve()