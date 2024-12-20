import sys
input = sys.stdin.readline

HORIZONTAL = 0
VERTICAL = 1

def solve():
    N = int(input())
    
    world = [ [*map(int, input().split())] for _ in range(N)]
    
    def toggle_horizontal(world, i):
        for x in range(N):
            world[i][x] ^= 1
        
    def toggle_vertical(world, i):
        for x in range(N):
            world[x][i] ^= 1
    
    def check(origin_world):
        
        ans = N + N + N * N
        MAX_BITS = 1 << N
        for i in range(0,MAX_BITS):
            for j in range(0,MAX_BITS):
                world = [l[:] for l in origin_world]
                cnt = 0
                for k in range(N):
                    if i & (1 << k):
                        toggle_horizontal(world, k)
                        cnt += 1
                    if j & (1 << k):
                        toggle_vertical(world, k)
                        cnt += 1
                        
                cnt_1 = 0
                for ii in range(N):
                    cnt_1 += sum(world[ii])
                cnt += min(cnt_1, N*N - cnt_1)
                ans = min(ans, cnt)
        return ans
    
    print(check(world))
        
        

solve()

