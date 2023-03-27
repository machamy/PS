N = int(input())
guilty = [*map(int,input().split())]
arr = [[*map(int,input().split())] for _ in range(N)]
visit = [False for _ in range(N)]
ej = int(input())
survive = N

def dfs(day,mafia,survive,guilty):
    