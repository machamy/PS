import sys

input = sys.stdin.readline


D4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve():
    H, W = map(int, input().split())
    R, C, D = map(int, input().split())

    A = [list(map(int, input().rstrip())) for _ in range(H)]
    B = [list(map(int, input().rstrip())) for _ in range(H)]

    # 0 : U
    # 1 : R
    # 2 : D
    # 3 : L@

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
    while True:
        # 1. 현재 칸에 먼지가 있다면 제거
        if A[i][j] != -1:
            # 2-1. 제거했다면 A 규칙 만큼 회전
            rotate(A[i][j])
            A[i][j] = -1  # 제거
            last_mov = mov
            # 기억 지우기
        else:
            if last_mov < visited[i][j][dir]:
                # 한번더 방문했는데, 먼지 청소 안했음... last_mov가 더낮아버림..
                # 4-2 루프면 작동중지
                break
            else:
                # 루프가 아니면 해당 위치와 방향에 현재 mov를 기억
                visited[i][j][dir] = mov

            # 2-2. 이미 먼지가 없으면 B 참조. 해당 숫자만큼 회전
            rotate(B[i][j])
        # 3. 전진
        i += D4[dir][0]
        j += D4[dir][1]
        mov += 1
        # 4-1. 영역 밖이면 작동 중지
        if i < 0 or i >= H or j < 0 or j >= W:
            break

    print(last_mov)


solve()
