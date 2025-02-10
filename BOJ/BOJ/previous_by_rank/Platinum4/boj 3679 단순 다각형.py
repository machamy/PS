import sys
from functools import cmp_to_key
input = sys.stdin.readline
#print = sys.stdout.write

T = int(input())

def ccw(p1, p2, p3):
    """
    방향 판별
    p1->p2 벡터와
    p1->p3 벡터를 비교
    1: 반시계방향
    0: 일직선
    -1: 시계방향
    """
    x1, y1, _ = p1
    x2, y2, _ = p2
    x3, y3, _ = p3
    val = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0

def dist(p1, p2):
    x1, y1, _ = p1
    x2, y2, _ = p2
    return (x1-x2)**2 + (y1-y2)**2



# 계속 반시계방향으로만 선을 연결하자
# 시작점 기준...
# 1. 가장 왼쪽, 그리고 아래의 점을 고르고
# 2. 그 점을 기준으로 오른쪽 아래점부터 위로 쭉쭉쭉
# 3. 각도가 같으면 가까운거부터 ㄱㄱ (뻗어 나가야함)
# 마지막 연결점들은 거리가 먼 순서부터 연결해야함
def solve(points):
    min_point = min(points)
    def cmp(p1, p2):
        # 기준점과의 각도 비교
        nonlocal min_point
        val = ccw(min_point, p1, p2)
        if val == 0:
            return dist(min_point, p1) - dist(min_point, p2)
        return -val

    points.sort(key=cmp_to_key(cmp))
    # print(f"{points[0][2]=}  {min_point[2]=} \n")
    head = []
    tail = []
    for p in points:
        if ccw(min_point, points[-1], p) == 0:
            tail.append(p)
        else:
            head.append(p)
    print(' '.join(map(str, [p[2] for p in head+tail[::-1]])))
    

for _ in range(T):
    arr = list(map(int, input().split()))
    N = arr[0]
    points = [(arr[i], arr[i+1], i//2) for i in range(1, 2*N+1, 2)]
    solve(points)