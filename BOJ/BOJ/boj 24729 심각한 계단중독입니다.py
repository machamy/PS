import sys
MAX_NUM = 1000000

input = sys.stdin.readline
sys.setrecursionlimit(MAX_NUM+10)

def solve():
    N = int(input())
    A = [*map(int,input().split())]
    nums = [0 for _ in range(MAX_NUM+1)]
    remain = 0
    min_num = MAX_NUM+1
    for a in A:
        min_num = min(min_num,a)
        nums[a] += 1
        remain += 1
    
    def dfs(x, remain):
        nonlocal min_num,nums
        if remain == 0:
            if x == min_num:
                return True
            else:
                return False
            
        
        for nxt in [x+1, x-1]:
            if nxt < 0 or nxt > MAX_NUM:
                continue
            nums[nxt] -= 1
            if dfs(nxt,remain-1):
                return True
            nums[nxt] += 1
        return False
    
    if dfs(min_num,remain):
        print(1)
    else:
        print(-1)

solve()