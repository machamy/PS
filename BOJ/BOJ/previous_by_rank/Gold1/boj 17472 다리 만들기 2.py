import sys

input = sys.stdin.readline

D4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solve():
    N, M = map(int, input().split())
    world = [[*map(int, input().split())] for _ in range(N)]
    graphs = set()

    def print_world():
        nonlocal world
        for l in world:
            print(*map(lambda x: x - 10 if x > 1 else x, l))

    def add_edge(a, b, cost):
        nonlocal graphs
        if b > a:
            a, b = b, a
        # print(f"add_edge({a}, {b}, {cost})")
        if cost < 2:
            return
        graphs.add((a, b, cost))

    def make_island(i, j):
        nonlocal world
        make_island.island_count += 1
        s = [(i, j)]
        while s:
            i, j = s.pop()
            if world[i][j] != 1:
                continue
            world[i][j] = make_island.island_count + 10
            for di, dj in D4:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                s.append((ni, nj))

    make_island.island_count = 0

    vertical_prev = [None for _ in range(M)]
    for i in range(N):
        horizontal_prev = None
        # print(f"i: {i-1}, {vertical_prev}")
        for j in range(M):
            if world[i][j] == 1:
                make_island(i, j)
            if world[i][j] > 1:
                # 현재 위치에 섬이 있음

                if horizontal_prev is not None:
                    # 이전 섬이 있으면(가로)
                    if world[i][horizontal_prev] == world[i][j]:
                        # 같으면 이전 j 갱신
                        horizontal_prev = j
                    else:
                        # 다르면 간선 추가 및 갱신
                        add_edge(
                            world[i][j],
                            world[i][horizontal_prev],
                            abs(horizontal_prev - j) - 1,
                        )
                        horizontal_prev = j
                else:
                    horizontal_prev = j

                if vertical_prev[j] is not None:
                    # 이전 섬이 있으면(세로)
                    if world[vertical_prev[j]][j] == world[i][j]:
                        # 같으면 이전 j 갱신
                        vertical_prev[j] = i
                    else:
                        # 다르면 간선 추가 및 갱신
                        # print(
                        #     f"add_edge({world[i][j]-10}, {world[vertical_prev[j]][j]-10}, {abs(vertical_prev[j] - i) - 1})"
                        # )
                        add_edge(
                            world[i][j],
                            world[vertical_prev[j]][j],
                            abs(vertical_prev[j] - i) - 1,
                        )
                        vertical_prev[j] = i
                else:
                    vertical_prev[j] = i
    # print(f"i: {i}, {vertical_prev}")
    sorted_graphs = sorted(graphs, key=lambda x: x[2])
    # print(sorted_graphs)
    # print_world()
    prnts = [i for i in range(7)]

    # 크루스칼 알고리즘을 위한 유니온 파인드
    def union(a, b):
        nonlocal prnts
        a = find(a)
        b = find(b)
        if a == b:
            return

        if a < b:
            prnts[b] = a
        else:
            prnts[a] = b

    def find(a):
        nonlocal prnts
        if prnts[a] == a:
            return a
        prnts[a] = find(prnts[a])
        return prnts[a]

    # 크루스칼
    result = 0
    for a, b, cost in sorted_graphs:
        if find(a - 10) != find(b - 10):
            union(a - 10, b - 10)
            result += cost
    # 만약 MST가 아니면 -1 출력
    for i in range(1, make_island.island_count):
        if find(i) != find(i + 1):
            result = -1
            break
    print(prnts)
    print(result)


solve()
