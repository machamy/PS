N = input()

cnt = [0] * 10
total = len(N)
for i in range(len(N)):
    cnt[int(N[i])] += 1
N = int(N)
def recusive(n,remain):
    if remain == 0:
        if n > N:
            return n
        return False
    
    for nxt in range(10):
        if cnt[nxt] == 0:
            continue
        cnt[nxt] -= 1
        res = recusive(n*10+nxt, remain-1)
        if res:
            return res
        cnt[nxt] += 1

if ans := recusive(0, total):
    print(ans)
else:
    print(0)