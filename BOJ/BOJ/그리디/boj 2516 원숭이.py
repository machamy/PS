import sys

input = sys.stdin.readline

N = int(input())

data = [None for _ in range(N+1)]
for i in range(1,N+1):
    n,*arr = map(int,input().split())
    data[i] = arr

cage_A = [True for _ in range(N+1)]
cage_B = [False for _ in range(N+1)]
flag = True
while flag:
    flag = False
    for i in range(1,N+1):
        if cage_A[i]:
            cnt = 0
            for other in data[i]:
                if cage_A[other]:
                    cnt += 1
                    if cnt == 2:
                        cage_A[i] = False
                        cage_B[i] = True
                        flag = True
                        break
    for i in range(1,N+1):
        if cage_B[i]:
            cnt = 0
            for other in data[i]:
                if cage_B[other]:
                    cnt += 1
                    if cnt == 2:
                        cage_B[i] = False
                        cage_A[i] = True
                        flag = True
                        break
        

ans_A = [i for i in range(1,N+1) if cage_A[i]]
ans_B = [i for i in range(1,N+1) if cage_B[i]]

print(len(ans_A),*ans_A)
print(len(ans_B),*ans_B)