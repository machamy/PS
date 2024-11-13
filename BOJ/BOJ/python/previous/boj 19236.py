import sys
from copy import deepcopy

input = sys.stdin.readline

D8 = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

DEAD = 0

def solve():
    initial_input = [list(map(int, input().split())) for _ in range(4)]
    table = [[list() for _ in range(4)] for _ in range(4)]

    def init_fish():
        """
        data : [번호, 방향, 행, 열]
        번호가 0 일 경우 죽은상태.
        """
        for i in range(4):
            for j in range(4):
                number, direction = initial_input[i][j * 2], initial_input[i][j * 2 + 1] - 1
                data = [number, direction, i, j]
                table[i][j] = data

    init_fish()

    def dfs(shark, table):
        eat(shark, table)

        result = shark[0]
        fish_move(shark, table)

        for d in range(1,4):
            ni, nj = shark[2] + D8[shark[1]][0] * d, shark[3] + D8[shark[1]][1] * d
            if 0 <= ni < 4 and 0 <= nj < 4 and table[ni][nj][0] != DEAD:
                result = max(dfs([shark[0], shark[1], ni, nj], deepcopy(table)), result)
        return result

    def eat(shark, table):
        """
        i,j 에 있는 물고기를 먹는 함수
        """
        i,j = shark[2:4]
        data = table[i][j]
        shark[0] += data[0]
        data[0] = DEAD
        shark[1] = data[1]

    def fish_move(shark, table):
        fishes = []
        for i in range(4):
            for j in range(4):
                if table[i][j][0] != DEAD:
                    fishes.append(table[i][j])
        fishes.sort()

        for f in fishes:
            number, direction, *pos = f

            # 이동이 가능할 때 까지 빙글빙글 돈다
            while True:
                ni, nj = pos[0] + D8[f[1]][0], pos[1] + D8[f[1]][1]

                if 0 <= ni < 4 and 0 <= nj < 4:
                    # 상어가 아닐경우 교체
                    if not (ni == shark[2] and nj == shark[3]):
                        another = table[ni][nj]
                        f[2:4], another[2:4] = another[2:4], f[2:4]
                        table[ni][nj], table[pos[0]][pos[1]] = f, another
                        break

                # 앞이 막힌 경우 돌린다
                f[1] = (f[1] + 1) % 8
                # 움직이지 않는 경우
                if direction == f[1]:
                    break
        fishes.sort()


    """
    shark : [점수, 방향, 행,열]
    """
    shark = [0, 0, 0, 0]

    print(dfs(shark, table))


solve()
