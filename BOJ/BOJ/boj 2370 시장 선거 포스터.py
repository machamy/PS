import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    
    coords = set()
    coord_dict = {}
    posters = [None] * N
    for i in range(N):
        l,r = map(int, input().split())
        coords.add(l)
        coords.add(r)
        posters[i] = (l,r)
        
    coords = sorted(list(coords))
    for i,e in enumerate(coords):
        coord_dict[e] = i
    
    wall = [0] * len(coords)
    for i in range(N):
        l,r = posters[i]
        l = coord_dict[l]
        r = coord_dict[r]
        for j in range(l,r+1):
            wall[j] = i
    
    visibles = set()
    for i in range(len(coords)):
        visibles.add(wall[i])
    print(len(visibles))
        
        
solve()