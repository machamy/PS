import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    points_X = [[*map(int,input().split())] for _ in range(n)]
    points_Y = [sorted(points_X, key = lambda x : [x[1],x[0]])]
    points_X = points_X.sort()
    ans = 40000 ** 2

    def get_dist(a,b):
        return (a[0]-b[0])**2 + (a[1]-b[1])**2

    for i, a in enumerate(points_X):
        pass


    print(ans)
solve()