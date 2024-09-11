import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write


def solve():
    N, T, W = map(int, input().split())

    # 대기열 = [id, 남은 시간]
    waiting = deque(list(map(int, input().split())) for _ in range(N))

    M = int(input())
    # 고객 = [id, 남은 시간, 영업 시작후 들어오는 시간]
    customer = [list(map(int, input().split())) for _ in range(M)]
    customer.sort(key=lambda x: -x[2])  # 시간에 따라 정렬한다.

    elapsed = 0
    while elapsed < W:
        e = waiting.popleft()

        if e[1] < T:
            # 한번에 처리하는 경우
            elapsed += e[1]
            print((str(e[0])+"\n") * e[1])
            e[1] = 0
        else:
            # 줄을 다시 서는 경우
            e[1] -= T
            elapsed += T
            print((str(e[0]) + "\n") * T)

        # 대기열에 추가할 목록
        temp = []
        while customer and customer[-1][2] <= elapsed:
            temp.append(customer.pop())
            temp.sort(key=lambda x: -x[2])

        while temp:
            waiting.append(temp.pop())

        # 되돌아 가는 경우 가장 뒤로 선다.
        if e[1]:
            waiting.append(e)



if __name__ == "__main__":
    solve()
