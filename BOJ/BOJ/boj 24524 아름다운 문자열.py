
S = input()
T = input()

ans = 0
cnt = [0] * len(T)

for i,e in enumerate(S):
    for j in range(len(T)-1):
        if e == T[j]:
            if j == 0:
                cnt[j] += 1
            if j > 0 and cnt[j-1] > cnt[j]:
                cnt[j] += 1
            break
        if cnt[j] == 0:
            break
    else:
        if e == T[-1]:
            for j in range(len(T)-1):
                cnt[j] -= 1
            ans += 1

print(ans)
