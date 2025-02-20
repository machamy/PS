import sys

N = int(input())
A = list(map(int,input().split()))
log_N = N.bit_length()

def shuffle(arr,k):
    length = len(arr)
    # print(arr)
    for i in range(k,-1,-1):
        amount = 1 << i
        # print(f"{amount=}")
        arr[:length] = arr[length-amount:length] + arr[:length-amount] 
        length = amount
        # print(arr)

# arr = list(range(1,6))
# shuffle(arr,2)

for i in range(1,log_N):
    for j in range(1,log_N):
        arr = list(range(1,N+1))
        shuffle(arr,i)
        shuffle(arr,j)
        # print(A,arr)
        if arr == A:
            print(i,j)
            exit()

assert()