import sys

input = sys.stdin.readline

"""
8 17 26 18 9
9 29 47 38 18
10 38 62 52 24
2 21 36 34 15
1 9 15 14 6

0 0 0 0 0
0 8 9 9 0
0 1 11 9 0
0 1 8 6 0
0 0 0 0 0

ans[1][1] = world[1-d][1-d] # 왼쪽위만
ans[1][2] = world[1-d][2-d] - world[1][2-d] # 왼쪽위 - 왼쪽왼쪽위 9 = 17 - 8
ans[1][3] = world[1-d][3-d] - world[1][2-d] # 9 = 26 - 17

ans[2][1] = world[2-d][1-d] - world[2-d-1][2-d] # 8 = 9 - 1
ans[2][2] = world[2-d][2-d] - world[2-d][2-d] - world[2][2-d-1] + world[2-d-1][2-d-1] # 11 = 29 - 9 - 17 + 8
ans[2][3] = world[2-d][3-d] - world[2-d][3-d] - world[2][2-d] + world[2-d-1][2-d] # 9 = 47 - 38 - 26 + 17

ans[3][1] = world[3-d][1-d] - world[3-d-1][1-d] # 1 = 10 - 1
ans[3][2] = world[3-d][2-d] - world[3-d-1][2-d] - world[3][2-d-1] + world[3-d-1][2-d-1] # 8 = 38 - 29 - 26 + 17
ans[3][3] = world[3-d][3-d] - world[3-d-1][3-d] - world[3][3-d-2] + world[3-d-1][2-d-1] # 6 = 62 - 47 - 36 + 26



 8 17 26 19 21 21 21 18  9  8
14 36 56 43 40 39 42 36 17 13
20 50 70 53 46 54 60 59 31 22
22 48 70 55 48 48 53 48 26 14
18 33 52 50 60 66 68 64 39 21
17 31 63 62 69 53 51 45 29 15
13 31 59 71 75 66 53 54 35 23
12 37 60 65 53 49 38 43 24 18
 7 25 35 43 38 47 37 39 20 15
 1 10 13 13  9 19 21 23 10  7

0  0  0  0  0  0  0  0  0  0
0  8  9  9  1 11  9  1  8  0
0  6 13 11  0  8 10  3  5  0
0  6  8  0  2  4  9  5  9  0
0 10  5 11  5  7  3  4  0  0
0  2  2  8  9 14 13  9 12  0
0  5  7 13  2  0  0  1  3  0
0  6  9  7 14  8  6  2  8  0
0  1  9  3  1  5 13  3  7  0
0  0  0  0  0  0  0  0  0  0

7 = 43 - 54 - 38 + 38 + 5 + 3 - 0 # 오른쪽 맨 아래 폭탄

ans[1][1] = world[1-d][1-d] # 왼쪽위만 8
ans[1][2] = world[1-d][2-d] - world[1][2-d] # 왼쪽위 - 왼쪽왼쪽위 9 = 17 - 8
ans[1][3] = world[1-d][3-d] - world[1][2-d] # 9 = 26 - 17
ans[1][4] = world[1-d][4-d] - world[1][3-d] + ans[1][4-3] # 1 = 19 - 9 + 8
ans[1][5] = world[1-d][5-d] - world[1][4-d] + ans[1][5-3] # 11 = 21 - 21 + 1
ans[1][6] = world[1-d][6-d] - world[1][5-d] + ans[1][6-3] # 9 = 21 - 21 + 11
ans[1][7] = world[1-d][7-d] - world[1][6-d] + ans[1][7-3] # 1 = 21 - 21 + 9
ans[1][8] = world[1-d][8-d] - world[1][7-d] + ans[1][8-3] # 8 = 18 - 18 + 1

ans[2][1] = world[2-d][1-d] - world[2-d-1][2-d] # 6 = 14 - 8
ans[2][2] = world[2-d][2-d] - world[2-d][2-d] - world[2][2-d-1] + world[2-d-1][2-d-1] # 13 = 36 - 17 - 26 + 9
ans[2][3] = world[2-d][3-d] - world[2-d][3-d] - world[2][2-d] + world[2-d-1][2-d] # 11 = 56 - 38 - 52 + 26
ans[2][4] = world[2-d][4-d] - world[2-d][4-d] - world[2][3-d] + world[2-d-1][3-d] + ans[2][4-3] # 0 = 43 - 43 - 50 + 50 + 6
ans[2][5] = world[2-d][5-d] - world[2-d][5-d] - world[2][4-d] + world[2-d-1][4-d] + ans[2][5-3] # 8 = 40 - 40 - 60 + 60 + 0
ans[2][6] = world[2-d][6-d] - world[2-d][6-d] - world[2][5-d] + world[2-d-1][5-d] + ans[2][6-3] # 10 = 39 - 39 - 66 + 66 + 8
ans[2][7] = world[2-d][7-d] - world[2-d][7-d] - world[2][6-d] + world[2-d-1][6-d] + ans[2][7-3] # 3 = 42 - 42 - 68 + 68 + 10
ans[2][8] = world[2-d][8-d] - world[2-d][8-d] - world[2][7-d] + world[2-d-1][7-d] + ans[2][8-3] # 5 = 36 - 36 - 64 + 64 + 3

ans[3][1] = world[3-d][1-d] - world[3-d-1][1-d] # 6 = 20 - 14
...
ans[3][8] = world[3-d][8-d] - world[3-d][8-d] - world[3][7-d] + world[3-d-1][7-d] + ans[3][8-3] # 9 = 31 - 31 - 36 + 36 + 8

"""

def solve():
    N, M = map(int, input().split())

    world = [[*map(lambda x: -int(x), input().split())] for _ in range(N)]

    # sums = [[0 for _ in range(N)] for _ in range(N)]
    ans = [[0 for _ in range(N)] for _ in range(N)]

    d = M // 2
    for i in range(d, N - d):
        for j in range(d, N - d):
            
            # 왼쪽 위 값
            ans[i][j] = world[i-d][j-d]
            
            if i - d - 1 >= 0:
                # 왼쪽 위위값
                ans[i][j] -= world[i - d - 1][j - d]
            if j - d - 1 >= 0:
                # 왼쪽왼쪽 위값 
                ans[i][j] -= world[i - d][j - d - 1]
            if i - d - 1 >= 0 and j - d - 1 >= 0:
                # 왼쪽왼쪽 위위 값
                ans[i][j] += world[i - d - 1][j - d - 1]
                
            # 첫줄의 경우는 아래는 실행 안됨
            if i - M >= 0:
                ans[i][j] += ans[i - M][j]
            if j - M >= 0:
                ans[i][j] += ans[i][j - M]
            if i - M >= 0 and j - M >= 0:
                ans[i][j] -= ans[i - M][j - M]


    print("---")
    for l in world:
        print(*l)
    print("---")
    for l in ans:
        print(*l)


solve()
