import sys

input = sys.stdin.readline


class Segmant:
    """
    세그먼트 트리
    """

    def __init__(self, data):
        self.data = data
        self.num = len(data)
        self.size = 2 << self.num.bit_length()
        self.tree = [1 for _ in range(self.size)]
        self.initialize(1, 0, self.num - 1)

    def initialize(self, node, start, end):
        """
        tree[node] : start~end까지의 합
        start == end 면 데이터와 같다
        """
        if start == end:
            self.tree[node] = (self.data[start], start)
            return

        self.initialize(node * 2, start, (start + end) // 2)
        self.initialize(node * 2 + 1, (start + end) // 2 + 1, end)
        self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, left, right, node, start, end):
        if left > end or right < start:
            return (float("inf"),-1)
        if left <= start and end <= right:
            return self.tree[node]
        lsum = self.query(left, right, node * 2, start, (start + end) // 2)
        rsum = self.query(left, right, node * 2 + 1, (start + end) // 2 + 1, end)
        return min(lsum, rsum)

    def update(self, idx, num, node, start, end):
        if idx < start or idx > end:
            return
        if start == end:
            self.tree[node] = (num, idx)
            return
        self.update(idx, num, node * 2, start, (start + end) // 2)
        self.update(idx, num, node * 2 + 1, (start + end) // 2 + 1, end)
        self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])


N = int(input())
data = [*map(int, input().split())]
M = int(input())

seg = Segmant(data)
for _ in range(M):
    cmd, b, c = map(int, input().split())
    if cmd == 1:
        seg.update(b - 1, c, 1, 0, seg.num - 1)
    elif cmd == 2:
        print(seg.query(b - 1, c - 1, 1, 0, seg.num - 1)[1]+1)