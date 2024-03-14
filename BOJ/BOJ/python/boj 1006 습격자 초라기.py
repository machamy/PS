import sys

input = sys.stdin.readline

def solve():
    global enemy, a,b,c, N, W
    N, W = map(int,input().split())
    enemy = [list(map(int,input().split())) for _ in range(2)]

    a = [0] * N # ┏ 모양
    b = [0] * N # ┗ 모양
    c = [0] * (N+1) # ┃ 모양

    a[0] = 1
    b[0] = 1
    c[0] = 0
    calc(0)
    result = c[N]

    if(N == 1):
        print(result)
        return

    if(enemy[0][0] + enemy[0][-1] <= W):
        a[1] = 2
        b[1] = 1 if enemy[1][0] + enemy[1][1] <= W else 2
        c[1] = 1
        calc(1)
        result = min(result, b[N-1] + 1)
    if(enemy[1][0] + enemy[1][-1] <= W):
        a[1] = 1 if enemy[0][0] + enemy[0][1] <= W else 2
        b[1] = 2 
        c[1] = 1
        calc(1)
        result = min(result, a[N-1] + 1)
    if(enemy[0][0] + enemy[0][-1] <= W and enemy[1][0] + enemy[1][-1] <= W):
        a[1] = 1
        b[1] = 1
        c[1] = 0
        calc(1)
        result = min(result,c[N-1] + 2)
    


    print(result)
def calc(start):
    global enemy, a,b,c, N, W
    for i in range(start, N):
        # C 확인
        c[i+1] = min(a[i] + 1, b[i] + 1) # 기본

        if(          enemy[0][i] + enemy[1][i] <= W):
            # C => C 두개 커버
            c[i+1] = min(c[i+1],c[i] + 1)
        if(i > 0 and enemy[0][i-1] + enemy[0][i] <= W 
                 and enemy[1][i-1] + enemy[1][i] <= W):
            # C => C 네개 커버
            c[i+1] = min(c[i-1] + 2, c[i+1])


        if i >= N-1:
            continue
        
        # A 확인
        a[i+1] = c[i+1] + 1 # 기본
        if(enemy[0][i] + enemy[0][i+1] <= W):
            # 하나 or 두개 커버
            a[i+1] = min(a[i+1] ,b[i] + 1)

        # B 확인
        b[i+1] = c[i+1] + 1 # 기본
        if(enemy[1][i] + enemy[1][i+1] <= W):
            # 하나 or 두개 커버
            b[i+1] = min(b[i+1] , a[i] + 1)




for _ in range(int(input())):
    solve()