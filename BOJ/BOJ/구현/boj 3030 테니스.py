import sys
input = sys.stdin.readline


F = 'federer'
x,y = input().split()

def is_vaild(idx,a,b):
    if a < 6 and b < 6:
        return False
    if idx <= 1:
        # 1,2라는 듀스 X
        if a == 7 and not (5 <= b <= 6):
            return False
        if not (5 <= a <= 6) and b == 7:
            return False
        if a >= 8 or b >= 8:
            return False
    else:
        if a >= 6 and b >= 6:
            # 듀스
            if abs(a-b) < 2:
                return False
    # if abs(a-b) >= 3:
    #     return False
        
    return True

def get_result(idx,a,b):
    if idx <= 1:
        if a < b:
            return 1
        elif a == b:
            return 0
        else:
            return -1
    if abs(a-b) <= 1:
        return 0
    if a < b:
        return 1
    else:
        return -1
def solve():
    matches = input().split()
    data = [] # -1 0 1
    wins = [0,0,0]
    for idx,m in enumerate(matches):
        if wins[-1] == 2 or wins[1] == 2:
            # 경기 끝났는데 계속함
            return False
        a,b = map(int,m.split(":"))
        if not is_vaild(idx,a,b):
            return False
        res = get_result(idx,a,b)
        wins[res] += 1
        data.append(res)
        if res == 0:
            assert False

        if res == -1 and y == "federer":
            return False
        if res ==  1 and x == "federer":
            return False
    if wins[1] <= 1 and wins[-1] <= 1:
        return False
    return True
    

for _ in range(int(input())):
    print("da" if solve() else "ne")