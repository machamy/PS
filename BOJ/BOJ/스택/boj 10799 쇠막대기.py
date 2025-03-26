

S = input()
ans = 0
cnt = 0
for i,e in enumerate(S):
    print(i,cnt,ans)
    if e == "(":
        cnt += 1
        ans += 1
        continue
    if S[i-1] == "(":
        # 레이저임
        cnt -= 1
        ans -= 1
        ans += cnt
    else:
        # 레이저가 아니라 막대의 끝임
        cnt -= 1
print(ans)