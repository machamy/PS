import sys

input = sys.stdin.readline

def solve():
    a,b,r,x,y,rr = map(int,input().split())

    
    dist2 = (a-x) ** 2 + (b-y) ** 2
    checkdist2 = (rr + r) ** 2
    dist = dist2 ** 0.5
    diff = abs(r-rr)

    if dist2 == 0 and r == rr:
        return -1
    

    if dist2 > checkdist2:
        # 멀리 있는 경우
        return 0
    if dist2 == checkdist2:
        # 외접할 경우
        return 1
    if dist == diff:
        # 내접할경우
        return 1
    if dist < diff:
        return 0
    return 2

for _ in range(int(input())):
    print(solve())