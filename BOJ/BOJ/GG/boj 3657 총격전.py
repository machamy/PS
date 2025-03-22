import math
import sys

# 거리 계산 함수
def calc_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def solve():
    n, m = map(int, input().split())  # 사람의 수 n, 진술의 수 m
    names = []  # 사람들의 이름을 저장
    positions = {}  # 사람들의 위치 정보 저장
    idx_map = {}  # 이름을 인덱스로 매핑
    dist = [[float('inf')] * n for _ in range(n)]  # 시간 차이를 저장하는 행렬, 초기값은 무한대
    time = [[float('inf')] * n for _ in range(n)]  # 시간 차이 행렬

    for i in range(n):
        name, x, y = input().split()
        x, y = int(x), int(y)
        names.append(name)
        positions[name] = (x, y)
        idx_map[name] = i
        dist[i][i] = 0  # 자기 자신과의 거리 차이는 0
        time[i][i] = 0  # 자기 자신과의 시간 차이는 0

    # 진술 처리
    for _ in range(m):
        person1, _, person2, _, _, person3 = input().split()
        i = idx_map[person1]
        j = idx_map[person2]
        k = idx_map[person3]

        # 거리 차이 계산: dkj - dki
        dist_ik = calc_distance(*positions[person1], *positions[person2])  # i -> k 거리
        dist_jk = calc_distance(*positions[person1], *positions[person3])  # j -> k 거리

        # 시간 차이 계산: tij = dkj - dki
        time[j][k] = min(time[j][k], dist_jk - dist_ik)

    # Floyd-Warshall 알고리즘을 사용하여 시간 차이 행렬을 추론
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if time[i][k] != float('inf') and time[k][j] != float('inf'):
                    time[i][j] = min(time[i][j], time[i][k] + time[k][j])

    # 모순 검사: 자기 자신보다 더 늦게 쐈다면 불가능
    for i in range(n):
        if time[i][i] < 0:
            print("IMPOSSIBLE")
            return

    # 가능한 총 발사 순서를 찾기
    order = []
    for i in range(n):
        for j in range(n):
            if time[i][j] < 0:
                order.append(f"{names[i]} {names[j]}")

    if order:
        # 여러 사람이 관계된 순서를 출력
        for o in sorted(set(order)):
            print(o)
    else:
        # 가능한 순서가 없을 경우 "UNKNOWN"
        print("UNKNOWN")

# 테스트 케이스의 수
T = int(input())

for _ in range(T):
    solve()
