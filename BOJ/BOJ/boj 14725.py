import sys
from collections import deque, defaultdict

input = sys.stdin.readline


class Node:
    def __init__(self, key):
        self.key = key
        self.child = {}


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, arr):
        node = self.root

        for word in arr:
            if word not in node.child:
                node.child[word] = Node(word)
            node = node.child[word]


def dfs(node, depth):
    for k, e in sorted(node.child.items()):
        print('--' * depth + k)
        dfs(e, depth + 1)


def solve():
    N = int(input())
    trie = Trie()

    for _ in range(N):
        n, *arr = input().split()
        trie.insert(arr[::])

    dfs(trie.root, 0)


solve()
