import sys

sys.setrecursionlimit(5000)

arr = [list(map(int,input().split())) for _ in range(3)]

min_cost = float('inf')
TARGET = 15

def cost(a,b):
    return abs(a-b)

def check_horizon(i):
    return sum(arr[i]) == TARGET

def check_vertical(j):
    s = 0
    for i in range(3):
        s += arr[i][j]
    return s == TARGET

def check_diag_down():
    s = 0
    for i in range(3):
        s += arr[i][i]
    return s == TARGET

def check_diag_up():
    s = 0
    for i in range(3):
        s += arr[2-i][i]
    return s == TARGET

def check():
    res = all(check_horizon(i) for i in range(3)) and all(check_vertical(i) for i in range(3)) and check_diag_up() and check_diag_down()
    return res

def dfs(depth, cost, used):
    global min_cost
    if depth == 9 and check():
        min_cost = min(min_cost,cost)
    if cost > min_cost:
        return
    
    i,j = depth // 3, depth % 3
    for num in range(1,10):
        if used & (1 << num):
            continue
        nxt_cost = cost + abs(num - arr[i][j])
        tmp = arr[i][j]
        arr[i][j] = num
        if j == 2:
            if check_horizon(i) == False:
                arr[i][j] = tmp
                continue
        if i == 2:
            if check_vertical(j) == False:
                arr[i][j] = tmp
                continue
        dfs(depth+1,nxt_cost,used | (1 << num))
        arr[i][j] = tmp

dfs(0,0,0)
print(min_cost)