import sys

input = sys.stdin.readline


def solve():
    C, N = map(int, input().split())
    colors = [input().rstrip() for _ in range(C)]
    names = set(input().rstrip() for _ in range(N))



    def add_color(trie, color):
        current = trie
        for e in color:
            if e not in current:
                current[e] = {}
            current = current[e]

        current['END'] = True
    trie_name = {}
    trie_color = {}
    for c in colors:
        add_color(trie_color,c)
    for n in names:
        add_color(trie_name, n)

    def find(team):
        current = trie_color
        result = False
        for i, e in enumerate(team):
            if 'END' in current and team[i:] in names:
                return True
            if e not in current:
                return False
            current = current[e]
        return result


    Q = int(input())
    teams = [input().rstrip() for _ in range(Q)]

    for t in teams:
        print('Yes' if find(t) else 'No')

solve()
