

def solve():
    a,b,c,d,x,y,z,w = map(int, input().split())


    """
    직사각형 판정
    안겹치면 d
    점이 겹치면 c
    선이 겹치면 b
    나머진 a
    """
    if c < x or z < a or d < y or w < b:
        return 'd'
    if (c == x and d == y) or (c == x and w == b) or (a == z and d == y) or (a == z and w == b):
        return 'c'
    if c == x or a == z or d == y or w == b:
        return 'b'
    return 'a'


for _ in range(4):
    print(solve())