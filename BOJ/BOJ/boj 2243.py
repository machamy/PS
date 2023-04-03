import sys
from collections import deque, defaultdict

input = sys.stdin.readline

MAX = 1_000_001


def solve():
    N = int(input())
    cmds = [list(map(int, input().split())) for _ in range(N)]

    tree = [0] * (1 << (MAX.bit_length() + 1))

    def query(idx, target, start, end):
        """
        세그먼트 트리 쿼리 함수
        :param idx: 트리의 인덱스
        :param target: 원하는 순위
        :param start: 시작인덱스 
        :param end: 끝인덱스
        :return: 쿼리의 결과
        """
        if start == end:
            return start
        mid = (start + end) // 2
        if target <= tree[idx * 2]:
            return query(idx * 2, target, start, mid)
        else:
            return query(idx * 2 + 1, target - tree[idx*2], mid + 1, end)

    def update(idx, target, diff, start, end):
        """
        세그먼트 트리 업데이트 함수
        :param idx: 트리의 인덱스
        :param target: 대상의 점수
        :param diff: 사탕의 개수
        :param start: 시작인덱스
        :param end: 끝인덱스
        :return:
        """
        if target < start or target > end:
            return
        tree[idx] += diff
        if start == end:
            return

        mid = (start + end) // 2
        update(idx * 2, target, diff, start, mid)
        update(idx * 2 + 1, target, diff, mid + 1, end)

    for cmd, *opt in cmds:
        if cmd == 1:
            b, = opt
            res = query(1, b, 1, MAX)
            print(res)
            update(1, res, -1, 1, MAX)
        else:
            b, c = opt
            update(1, b, c, 1, MAX)


solve()
