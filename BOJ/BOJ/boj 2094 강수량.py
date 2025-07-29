import math

class MaxSegmentTree:
    
    def __init__(self, data):
        self.n = len(data)
        h = math.ceil(math.log2(self.n))
        self.size = 1 << (h+1)
        self.tree = [0] * (self.size)
        self.data = data
        self.build(1, 0, self.n - 1)


    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start][1]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self,node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_max = self.query(2 * node, start, mid, left, right)
        right_max = self.query(2 * node + 1, mid + 1, end, left, right)
        return max(left_max, right_max)
    
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        h = math.ceil(math.log2(self.n))
        self.size = 1 << (h+1)
        self.tree = [0] * (self.size)
        self.data = data
        self.build(1, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = 1
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_min = self.query(2 * node, start, mid, left, right)
        right_min = self.query(2 * node + 1, mid + 1, end, left, right)
        return left_min + right_min


def b_search(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid][0] < target:
            left = mid + 1
        elif arr[mid][0] == target:
            return mid
        else:
            right = mid 
    return right

def main():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_seg = MaxSegmentTree(data)
    cnt_seg = SegmentTree(data)

    M = int(input())
    for _ in range(M):
        Y,X = map(int, input().split())
        
        no_y = False
        no_x = False
        is_maybe = False
        # Y년 이후에, X전까지의 Max가 X년보다 작아야함.
        y_idx = b_search(data, Y)
        x_idx = b_search(data, X)
        
        """
        로직.
        1. Y년 이후에, X전까지의 Max가 X년보다 작아야함.
        2. Y년 이후에, X전까지의 카운트가 Y - X와 같아야함.

        예외 사항. 
        정확히 Y년 데이터가 존재하지 않는 경우
        정확히 X년 데이터가 존재하지 않는 경우
        
        """
        
        if y_idx == len(data):
            # Y년 이후 데이터가 아예 없으면 maybe 출력
            print("maybe")
            continue
        if data[y_idx][0] != Y:
            # Y년 데이터가 없으면 Y년 정보를 모르므로 
            y_idx -= 1
            no_y = True
        if x_idx == len(data):
            # X년 데이터가 아예 없으면 maybe 체크
            no_x = True
        elif data[x_idx][0] != X:
            no_x = True
            # x_idx += 1

        if no_y and no_x:
            print("maybe")
            continue

        # print(f"Y: {data[y_idx]}, X: {data[x_idx]}")
        # Y년보다 X년이 더 강수량이 많은경우
        if not no_y and not no_x and data[y_idx][1] < data[x_idx][1]:
            print("false")
            continue

        # Y년 이후에, X전까지의 최대값
        # print(f"Y_idx: {y_idx}, X_idx: {x_idx}")
        max_val = max_seg.query(1, 0, max_seg.n - 1, y_idx + 1, x_idx-1)
        # print(f"Max: {max_val}")
        if not no_x and max_val >= data[x_idx][1]:
            print("false")
            continue
        if not no_y and max_val >= data[y_idx][1]:
            print("false")
            continue

        # Y년 이후에, X전까지의 카운트
        cnt = cnt_seg.query(1, 0, cnt_seg.n - 1, y_idx + 1, x_idx-1)
        if cnt != X - Y - 1:
            is_maybe = True
        
        if no_y or no_x or is_maybe:
            print("maybe")
        else:
            print("true")

main()