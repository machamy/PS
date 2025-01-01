import sys
input = sys.stdin.readline
N = int(input())

MAX_HEIGHT = 1_000_000_000
buildings = list(map(int, input().split()))
degrees =[[-1 for _ in range(N)] for _ in range(N)]

def get_degree(i, j):
    if degrees[i][j] != -1:
        return degrees[i][j]
    degrees[i][j] = (buildings[j] - buildings[i]) / (j - i)
    return degrees[i][j]

def left(i):
    degree_min = MAX_HEIGHT
    cnt = 0
    for j in range(i-1, -1, -1):
        if get_degree(i, j) < degree_min:
            degree_min = get_degree(i, j)
            cnt += 1
    return cnt

def right(i):
    degree_max = -MAX_HEIGHT
    cnt = 0
    for j in range(i+1, N):
        if get_degree(i, j) > degree_max:
            degree_max = get_degree(i, j)
            cnt += 1
    return cnt


ans = 0
for i in range(N):
    ans = max(ans, left(i) + right(i))
    
print(ans)