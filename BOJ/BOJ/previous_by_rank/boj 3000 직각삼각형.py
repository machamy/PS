import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    vertical_points = dict()
    horizontals_points = dict()
    for _ in range(N):
        x, y = map(int, input().split())
        if x not in vertical_points:
            vertical_points[x] = []
        if y not in horizontals_points:
            horizontals_points[y] = []
        vertical_points[x].append(y)
        horizontals_points[y].append(x)
    
    res = 0
    for x,y_list in vertical_points.items():
        if len(y_list) < 2:
            continue
        for y in y_list:
            res += (len(horizontals_points[y]) - 1) * (len(y_list) - 1)
            
    print(res)
    
solve()