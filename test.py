


def matrixmult(n, A, B, C):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            C[i][j] = A[i][1] * B[1][j]
            for k in range(2, n + 1):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

n = 1

A = [[],[0,1, 2], [0,3, 4]]
B = [[],[0,1, 2], [0,3, 4]]
C = [[0] * (n+1) for _ in range(n+1)]

matrixmult(n,A,B,C)
print(C)