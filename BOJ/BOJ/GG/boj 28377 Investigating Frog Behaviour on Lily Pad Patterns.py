import sys

input = sys.stdin.readline
"""
5
1 2 3 5 7
4
2
1
5
2

4
2
6
8
"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class SortedSet:
    def __init__(self, arr):
        self.root = None
        for a in arr:
            self.insert(a)
        
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._minValueNode(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_min_greater_than(self, key):
        current = self.root
        candidate = None
        while current:
            if key < current.val:
                candidate = current.val
                current = current.left
            else:
                current = current.right
        return candidate


def solve():
    n = int(input()) # number of frogs
    arr = list(map(int, input().split())) # initial position of frogs
    q = int(input()) # number of jumps
    jumps = [int(input()) for _ in range(q)] # i th frog jumps... by time
    
    largest_pos = max(arr)
    # 모든 빈공간을 찾아서 넣어준다.
    empty = SortedSet(set(i for i in range(1, largest_pos)) - set(arr))
    

    for frog in jumps:
        # empty에 있는 값중, frog의 현재 위치보다 큰 값중 가장 작은 값을 찾는다.
        # 그 값을 frog의 위치로 바꿔준다.
        
        n = empty.find_min_greater_than(arr[frog-1])
        if n is None:
            n = largest_pos + 1
            largest_pos += 1
        empty.delete(n)
        empty.insert(arr[frog-1])
        arr[frog-1] = n
        print(n)
    
    
    

solve()