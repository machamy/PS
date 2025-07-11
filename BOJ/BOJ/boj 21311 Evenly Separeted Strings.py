
s = input()
if len(s) > 52:
    print("NO")
    exit()
cnt = [0 for _ in range(26)]
prev = [-1 for _ in range(26)]
for i,raw in enumerate(s):
    c = ord(raw) - ord('a')
    if prev[c] == -1:
        prev[c] = i
        cnt[c] += 1
        continue
    if (i - prev[c]) % 2 == 0:
        # 사이에 홀수개가 있음.
        print("NO")
        break
    cnt[c] += 1
    if cnt[c] == 3:
        print("NO")
        break
    
else:
    print("YES")