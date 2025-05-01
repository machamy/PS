import sys

input = sys.stdin.readline


def print_matrix(matrix):
    for x,cube in enumerate(matrix):
        print(f"cube {x}:")
        for y,layer in enumerate(cube):
            print(f"  Layer {y}:")
            for z, row in enumerate(layer):
                print(f"    Row {z}: {row}")
            print()
        print()


def solve():
    N,M,K,T = map(int, input().split())
    room = [[[[0 for _ in range(T)] for _ in range(K)] for _ in range(M)] for _ in range(N)]
    for x in range(N):
        for y in range(M):
            for z in range(K):
                line = list(map(int, input().split()))
                for w in range(T):
                    room[x][y][z][w] = line[w]
    sums = [[[[0 for _ in range(T)] for _ in range(K)] for _ in range(M)] for _ in range(N)]
    for x in range(N):
        for y in range(M):
            for z in range(K):
                for w in range(T):
                    sums[x][y][z][w] = room[x][y][z][w]
                    if x > 0:
                        sums[x][y][z][w] += sums[x-1][y][z][w]
                    if y > 0:
                        sums[x][y][z][w] += sums[x][y-1][z][w]
                    if z > 0:
                        sums[x][y][z][w] += sums[x][y][z-1][w]
                    if w > 0:  
                        sums[x][y][z][w] += sums[x][y][z][w-1]

    print_matrix(room)
    print_matrix(sums)



solve()