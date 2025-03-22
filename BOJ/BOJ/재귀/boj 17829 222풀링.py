import sys

input = sys.stdin.readline

def solve():
    N = int(input())

    arr = [[*map(int,input().split())] for _ in range(N)]


    def recursive(d,i0,j0,i1,j1):
        # print(f"{d=} {i0=},{j0=},{i1=},{j1=}")
        if d == 1:
            return arr[i0][j0]
        
        delta = (d) // 2 
        l = [recursive(delta,i0,j0,i0+delta,j0+delta),
             recursive(delta,i0+delta,j0,i0+d,j0+delta),
             recursive(delta,i0,j0+delta,i0+delta,j0+d),
             recursive(delta,i0+delta,j0+delta,i0+d,j0+d)
             ]
        l.sort()
        return l[-2]
    
    print(recursive(N,0,0,N-1,N-1))


solve()