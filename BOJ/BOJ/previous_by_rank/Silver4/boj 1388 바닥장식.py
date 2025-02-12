import sys

input = sys.stdin.readline




def solve():
    n, m = map(int, input().split())
    world = [input() for _ in range(n)]
    
    ans = 0
    verticals = [0 for _ in range(m)]
    for i in range(n):
        horizontal = 0
        for j in range(m):
            if world[i][j] == '-':
                horizontal += 1
                
                if verticals[j] > 0:
                    ans += 1
                verticals[j] = 0
            else:
                if horizontal > 0:
                    ans += 1
                horizontal = 0
                
                verticals[j] += 1
        if horizontal > 0:
            ans += 1
    for v in verticals:
        if v > 0:
            ans += 1
    
                
    print(ans)
            
    
    
solve()