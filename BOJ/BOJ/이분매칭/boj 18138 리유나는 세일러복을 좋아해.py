import sys

input = sys.stdin.readline



def solve():
    N,M = map(int,input().split())

    assign = [-1] * (M) # 카라가 어떤 옷과 매칭됐는지
    done = [False] * (M) # 해당 탐색에서, 카라의 i번을 고려함?
    shirts = [int(input()) for _ in range(N)]
    
    adj = [list() for _ in range(N)]
    for collar in range(M):
        collar_width = int(input())
        for idx, w in enumerate(shirts):
            if w/2 <= collar_width <= w * 3 / 4 or  w <= collar_width <= w * 5 / 4:
                adj[idx].append(collar)
    
    def dfs(clothes):
        for collar in adj[clothes]:
            # print(clothes,collar)
            if done[collar]:
                continue
            done[collar] = True
            if assign[collar] == -1 or dfs(assign[collar]):
                assign[collar] = clothes
                return True
            
        return False

    ans = 0
    for i in range(N):
        done = [False for _ in range(M)]
        if dfs(i):
            ans += 1

    return ans


print(solve())
