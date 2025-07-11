

D4 = [(1,0),(-1,0),(0,-1),(0,1)]

def solve():
    N,M,y,x,K = map(int,input().split())

    board = [list(map(int,input().split())) for _ in range(N)]
    die = [0,0,0,0,0,0]

    def roll(dir,die):
        if dir == 1: # 동쪽
            die[0], die[1], die[2], die[3], die[4], die[5] = die[3], die[1], die[0], die[5], die[4], die[2] 
        elif dir == 2: # 서쪽
            die[0], die[1], die[2], die[3], die[4], die[5] = die[2], die[1], die[5], die[0], die[4], die[3]
        elif dir == 3: # 북쪽
            die[0], die[1], die[2], die[3], die[4], die[5] = die[4], die[0], die[2], die[3], die[5], die[1] 
        elif dir == 4: # 남쪽
            die[0], die[1], die[2], die[3], die[4], die[5] = die[1], die[5], die[2], die[3], die[0], die[4]
        
    moves = [*map(int,input().split())]
    for move in moves:
        dx,dy = D4[move-1]
        nx,ny  = x + dx , y + dy
        if 0 <= ny < N and 0 <= nx < M:
            x,y, = nx,ny
            roll(move, die)
            if board[y][x] == 0: 
                board[y][x] = die[5]
            else :
                die[5] = board[y][x]
                board[y][x] = 0
            print(die[0])


solve()