
current = 1
for i in range(int(input())):
    a,b = map(int,input().split())
    if a == current:
        current = b
    elif b == current:
        current = a

print(current)