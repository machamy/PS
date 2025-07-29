
N = int(input())
"""
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711
"""
x = []
y = []

used12 = False
for i in range(N,2,-3):
    x.append(i)
    y.append(i-1)
    y.append(i-2)
    if i-1 == 2:
        used12 = True
    if i-2 == 2:
        used12 = True
if not used12:
    x.append(2)
    y.append(1)

print(len(x))
print(*x)
print(len(y))
print(*y)