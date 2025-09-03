N,M = map(int,input().split())
if N == 0:
    print(0)
    exit()
arr = list(map(int,input().split()))

box_cnt = 1
current_weight = 0

for w in arr:
    if current_weight + w <= M:
        current_weight += w
    else:
        box_cnt += 1
        current_weight = w

print(box_cnt)