import sys

input = sys.stdin.readline

sys.setrecursionlimit(500_002)

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
tree[0].append(1)
beauties = [None]+[list(map(int,input().split())) for _ in range(N)]

dp = [[0,0,0] for _ in range(N+1)]
path = [[0,0,0] for _ in range(N+1)]

def dfs(node,parent):
    dp[node][0] = beauties[node][0]
    dp[node][1] = beauties[node][1]
    dp[node][2] = beauties[node][2]
    for child in tree[node]:
        if child == parent:
            continue
        dfs(child,node)
        dp[node][0] += max(dp[child][1],dp[child][2])
        dp[node][1] += max(dp[child][0],dp[child][2])
        dp[node][2] += max(dp[child][0],dp[child][1])
color_name = ['R','G','B']
def check_color(node,node_color,prnt,colors):
    colors[node] = color_name[node_color]

    for child in tree[node]:
        if child == prnt:
            continue
        Max = -1
        Max_color = -1
        for child_color in range(3):
            if node_color == child_color:
                continue
            if dp[child][child_color] > Max:
                Max = dp[child][child_color]
                Max_color = child_color
        check_color(child,Max_color,node,colors)
    return colors



dfs(1,0)
print(max(dp[1]))
# print(dp[1])

colors = [0] *(N+1)
check_color(0,-1,-1,colors)

print(''.join(colors[1:]))