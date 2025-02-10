import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

class SegTree:

    # root = 1
    def __init__(self, size):
        self.num_arr = [0] * size
        self.size = size
        self.arr_size = 1 <<((size-1).bit_length()) + 1
        self.tree = [0] * (self.arr_size)
    
    
    def insert(self, target_idx, val):
        diff = val
        self.num_arr[target_idx] += val
        self.__insert_recursive(1, 0, self.size-1, target_idx, diff)

    def __insert_recursive(self, node, start, end, target_idx, diff):
        if target_idx < start or target_idx > end:
            return
        # print(node, start, end, target_idx, diff)
        self.tree[node] += diff
        if start == end:
            return
        
        mid = (start + end) // 2
        self.__insert_recursive(2 * node, start, mid, target_idx, diff)
        self.__insert_recursive(2 * node+1, mid + 1, end, target_idx, diff)

    def delete(self, val):
        self.__delete_recursivve(1, 0, self.size - 1, val)
    
    def __delete_recursivve(self, node, start, end, val):
        self.tree[node] -= 1
        if start == end:
            print(str(start + 1) + "\n")
            return
        # print(node, start, end, val)
        mid = (start + end) // 2
        left = self.tree[2 * node]
        if left >= val:
            # print(f"left: {left}, val: {val}")
            # 왼쪽 값이 더 크거나 같으면, 왼쪽을 탐색
            self.__delete_recursivve(2 * node, start, mid, val)
        else:
            # 오른쪽값이 더 크면, 오른쪽 탐색
            self.__delete_recursivve(2 * node + 1, mid + 1, end, val - left)

seg = SegTree(2_000_000)
for _ in range(N):
    T, X = input().split()
    if T == '1':
        seg.insert(int(X) - 1, 1)
    else:
        seg.delete(int(X))
    # for i in range(26):
    #     print(i,":",seg.tree[i])
    # # print(seg.num_arr[:11])