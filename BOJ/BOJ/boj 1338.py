
def solve():
    N,M = map(int,input().split())

    table = [[*input()] for _ in range(N)]

    for l in range(min(N,M),0,-1):
        for i in range(N-l):
            for j in range(M-l):
                if table[i][j] == table[i][j+l] and\
                        table[i][j] == table[i+l][j] and\
                        table[i][j] == table[i+l][j+l]:
                    print((l+1)**2)
                    return
    print(1)
solve()