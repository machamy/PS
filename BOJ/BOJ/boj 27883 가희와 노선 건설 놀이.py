import sys

input = sys.stdin.readline

def main():
    N,M = map(int,input().split())

    heights = [0 for _ in range(N+1)]
    replies = [int(input()) for _ in range(M)]

    MAX = 1
    cnt = 0
    turns = []
    turns.append("U 1 -10000")
    for rep in replies:
        MAX += 1
        target = rep+1
        heights[target] = MAX
        turns.append(f"U {target} {MAX}")
        turns.append(f"P")

    print(len(turns))
    for s in turns:
        print(s)


main()