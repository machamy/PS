import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
arr = [[i*N +j+1 for j in range(N)] for i in range(N)]
origin_examples = [
    [arr[0][0],0,0], # 홀 홀
    [arr[0][1],0,1], # 홀 짝
    [arr[1][0],1,0], # 짝 홀
    [arr[1][1],1,1]  # 짝 짝
]
examples = [
    [arr[0][0],0,0], # 홀 홀
    [arr[0][1],0,1], # 홀 짝
    [arr[1][0],1,0], # 짝 홀
    [arr[1][1],1,1]  # 짝 짝
]
row_buffer = [0,0]
column_buffer = [0,0]
def shift_rows():
    for e in examples:
        n,i,j = e
        e[2] = (j+row_buffer[i%2]) % N
    row_buffer[:] = 0,0

def shift_colmuns():
    for e in examples:
        n,i,j = e
        e[1] = (i+column_buffer[j%2]) % N
    
    column_buffer[:] = 0,0

swaps = []

state = 0
for _ in range(Q):
    cmd = input().split()

    if cmd[0] == "RE":
        row_buffer[1] += 1
        if state < 0:
            shift_colmuns()
        state = 1
            
    elif cmd[0] =="RO":
        row_buffer[0] += 1
        if state < 0:
            shift_colmuns()
        state = 1
            
    elif cmd[0] == "CE":
        column_buffer[1] += 1
        if state > 0:
            shift_rows()
        state = -1
            
    elif cmd[0] == "CO":
        column_buffer[0] += 1
        if state > 0:
            shift_rows()
        state = -1
    else:
        s,*nums = cmd
        a,b,i,j = map(int,nums)
        if state > 0:
            shift_rows()
        if state < 0:
            shift_colmuns()
        state = 0
        a,b,i,j = a-1,b-1,i-1,j-1
        
        ab_type = ij_type = -1
        for type,e in enumerate(examples):
            n,q,r = e
            if abs(a-q) % 2 == 0 and abs(b-r) % 2 == 0:
                ab_type = type
            if abs(i-q) % 2 == 0 and abs(j-r) % 2 == 0:
                ij_type = type
        ab = (ab_type,a-examples[ab_type][1],b-examples[ab_type][2])
        ij = (ij_type,i-examples[ij_type][1],j-examples[ij_type][2])
        swaps.append((ab,ij))


if state > 0:
    shift_rows()
if state < 0:
    shift_colmuns()

delta_examples = [[examples[type][0], examples[type][1]-origin_examples[type][1], examples[type][2]-origin_examples[type][2]] for type in range(4)]
for i in range(N):
    for j in range(N):
        current_num = i*N +j+1
        type = -1
        if i % 2 == 0:
            if j % 2 == 0:
                type = 0
            else:
                type = 1
        else:
            if j % 2 == 0:
                type = 2
            else:
                type = 3
        n,q,r = delta_examples[type]
        arr[(i+q)%N][(j+r)%N] = current_num
def get_lastpos(type,di,dj):
    return (examples[type][1] + di)%N, (examples[type][2] + dj)%N
for ab,ij in swaps:
    t_ab,da,db = ab
    t_ij,di,dj = ij
    a,b = get_lastpos(t_ab,da,db)
    i,j = get_lastpos(t_ij,di,dj)
    arr[i][j],arr[a][b] = arr[a][b],arr[i][j]
for l in arr:
    print(*l)