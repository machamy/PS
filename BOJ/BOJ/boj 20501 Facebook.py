import sys

input = sys.stdin.readline

N = int(input())
adj = [input() for _ in range(N)]
Q = int(input())

bitset = [[0 for _ in range(N//32 + 1)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if adj[i][j] == '1':
            bitset[i][j//32] |= (1 << (j % 32))
            
def get_cnt(a,b):
    cnt = 0
    for i in range(32):
        cnt += bin(bitset[a][i] & bitset[b][i]).count('1')
    return cnt

for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    res = 0
    res += get_cnt(a, b)
    print(res)