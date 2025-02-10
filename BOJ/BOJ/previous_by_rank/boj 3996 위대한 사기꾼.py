import sys

input = sys.stdin.readline
n,k = map(int,input().split())

ans = [0]

for i in range(1,n+1):
    a,b = divmod(i,k)
    x,y = divmod(i,-k)
    if x < 0 and y < 0:
        y += k
    if b == y :
        ans.append(i)

    
print(ans)
print(len(ans))