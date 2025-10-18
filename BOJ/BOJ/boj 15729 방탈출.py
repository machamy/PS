N = int(input())
arr = list(map(int, input().split()))

state = [0] * N

def click(pos):
    for i in range(pos, min(N, pos + 3)):
        state[i] = 1 - state[i]

cnt = 0
for i in range(N):
    if arr[i] != state[i]:
        click(i)
        cnt += 1

print(cnt)
