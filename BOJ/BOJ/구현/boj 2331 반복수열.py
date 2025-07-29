A, P = map(int, input().split())

D = {A : 0}
idx = 1
num = A
while True:
    nxt_num = 0
    while num > 0:
        m = num % 10
        nxt_num += m ** P
        num //= 10

    if nxt_num in D:
        print(D[nxt_num])
        break
    D[nxt_num] = idx
    idx += 1
    num = nxt_num