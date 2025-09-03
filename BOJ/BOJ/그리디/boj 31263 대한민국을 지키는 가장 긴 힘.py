MAX = 641

N = int(input())
S = input()

num = 0
cnt = 0
i = 0


while i < N:
    # print(i, S[i])
    if (i + 3 == N or (i + 3 < N and S[i+2] != "0")) and int(S[i:i+3]) <= MAX:
        i += 3
        cnt += 1
    elif (i + 2 == N or (i + 2 < N and S[i+1] != "0")) and int(S[i:i+2]) <= MAX:
        i += 2
        cnt += 1
    else:
        i += 1
        cnt += 1
        


print(cnt)
