N = int(input())
s = input()
song = list(s)
ans = 1
for i in range(1, N):
    if song[i] == s[0]:
        # 노래시작
        idx = 0
        for j in range(i+1, len(song)):
            idx += 1
            if song[j] != s[idx]:
                break
        else:
            song += s[idx+1:]
            ans += 1
# print(song)
print(ans)
