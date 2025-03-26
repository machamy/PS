
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

ans = []
a = b = 0
while a < N and b < M:
    a_nums = set(A[a:])
    b_nums = set(B[b:])

    common = a_nums & b_nums
    if not common:
        break
    Max = max(common)
    ans.append(Max)
    a = A.index(Max,a) + 1
    b = B.index(Max,b) + 1

print(len(ans))
if ans:
    print(*ans)