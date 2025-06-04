import sys

n = int(input())

ans = 0
for i in range(1,n):
    num = str(i) + str(i)[::-1]
    if int(num) <= n:
        ans += 1
    num = str(i)[:-1] + str(i)[::-1]
    if int(num) <= n:
        ans += 1
    
    if int(num) > n:
        break
print(ans)