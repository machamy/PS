import sys

input = sys.stdin.readline


D4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve():
    H, W = 4, 5
    R, C, D = 0, 3

    A = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    B = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    # 0 : U
    # 1 : R
    # 2 : D
    # 3 : L

    jump_table = [[[None for _ in range(4)] for _ in range(W)] for _ in range(H)]
    jump_costs = [[[0 for _ in range(4)] for _ in range(W)] for _ in range(H)]
    visited = [[[-1 for _ in range(4)] for _ in range(W)] for _ in range(H)]

    i, j = R, C
    dir = D

    def rotate(times):
        nonlocal dir
        return (dir := ((dir + times) % 4))

    # A[i][j]의 먼지를 청소하면, A[i][j] = -1

    mov = 1  # 마지막에 반드시 이동을 하므로, 1로 시작
    last_mov = mov
    # 1. 현재 칸에 먼지가 있다면 제거
    # 2. 제거했다면 A, 아니면 B 참조. 해당 숫자만큼 회전
    # 3. 전진

    path_stack = []

    while True:
        # 4-1. 영역 밖이면 작동 중지
        if i < 0 or i >= H or j < 0 or j >= W:
            # print(f"ended {i,j}")
            break

        # print(f"current {(i,j)}")
        # for l in A:
        #     print(l)

        # 1. 현재 칸에 먼지가 있다면 제거
        if A[i][j] != -1:
            # 먼지를 지웠다면, 점프테이블 수정
            current_cost = (
                jump_costs[i][j][dir] + 1
            )  # 첫 스택은 자기자신, 생략하는 느낌
            while path_stack:
                tmp_i, tmp_j, tmp_dir = path_stack.pop()
                jump_table[tmp_i][tmp_j][tmp_dir] = (i, j, dir)
                jump_costs[tmp_i][tmp_j][tmp_dir] += current_cost
                current_cost = jump_costs[tmp_i][tmp_j][tmp_dir] + 1
            # 2-1. 제거했다면 A 규칙 만큼 회전
            rotate(A[i][j])
            A[i][j] = -1  # 제거
            last_mov = mov

        else:
            # 이미 청소함
            if last_mov < visited[i][j][dir]:
                # 한번더 방문했는데, 먼지 청소 안했음... last_mov가 더낮아버림..
                # 4-2 루프면 작동중지
                break

            # 루프가 아니면 해당 위치와 방향에 현재 mov를 기억
            visited[i][j][dir] = mov
            path_stack.append((i, j, dir))  # 진입 상태 기억
            if jump_table[i][j][dir] is None:
                # 점프 테이블 없음
                rotate(B[i][j])
            else:
                # print(f"Jump from {(dir, i,j)} to {visited[i][j][dir]}")
                # 점프 테이블 있음
                i, j, dir = jump_table[i][j][dir]  # 점프
                mov += jump_costs[i][j][dir]
                rotate(B[i][j])
            # 2-2. 이미 먼지가 없으면 B 참조. 해당 숫자만큼 회전

        # 3. 전진
        i += D4[dir][0]
        j += D4[dir][1]
        mov += 1

    print(last_mov)


solve()
