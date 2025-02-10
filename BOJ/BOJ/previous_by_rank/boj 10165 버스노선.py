import sys 

input = sys.stdin.readline 

N = int(input())
M = int(input())

busses_A = []
busses_B = []
min_a = float('inf')
max_b = -1
for i in range(M):
    a,b = map(int,input().split())
    if a <= b:
        data = (a,b,i+1)
        busses_A.append(data)
    else:
        min_a = min(min_a,a)
        max_b = max(max_b,b)
        data = (a,b+N,i+1)
        busses_B.append(data)

def key_cmp(x):
    return (x[0],-x[1])

busses_A.sort(key= key_cmp)
busses_B.sort(key= key_cmp)
# A. a < b 인 경로
# B. a > b 인 경로

# 1. 모든 A 경로에 대해 겹치는 지 판정
# 2. 모든 B 경로에 대해 겹치는 지 판정
# 3. B에 포함되는 A경로 확인
# 4. A에 포함되는 B경로는 없음

right = -1
res = set()
for a,b,idx in busses_A:
    if min_a <= a:
        continue
    if max_b >= b :
        continue
    if b <= right:
        continue
    right = b
    res.add(idx)
    print(f"add a {idx}")

right = -1
for a,b,idx in busses_B:    
    if b <= right:
        continue
    right = b
    res.add(idx)
    print(f"add b {idx}")
    

print(*sorted(res))