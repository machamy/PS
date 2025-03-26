
s = list(input())
scores = []
frame = 0
num_flag = 0
bonus_idx = -1
for i,c in enumerate(s):
    n = 0
    if c == "S":
        n = 10
        frame += 1
        num_flag = 0
    elif c == "P":
        n = 10-scores[i-1]
        frame += 1
        num_flag = 0
    else:
        if c == "-":
            n = 0
        else:
            n = int(c)
        if num_flag == 0:
            num_flag = 1
        elif num_flag == 1:
            num_flag = 2
    scores.append(n)
    if num_flag == 2:
        frame += 1
        num_flag = 0

    if frame == 10 and bonus_idx == -1:
        bonus_idx = i
        

ans = 0
# print(scores)
# print(s)
last_idx = len(s) if bonus_idx == -1 else bonus_idx + 1
for i,c in enumerate(s[:last_idx]):
    ans += scores[i]
    if c == "S":
        ans += scores[i+1] + scores[i+2]
    elif c == "P":
        ans += scores[i+1]
    # print(i,c,ans)
print(ans)