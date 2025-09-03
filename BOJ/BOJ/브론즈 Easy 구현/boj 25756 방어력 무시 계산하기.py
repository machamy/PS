N = int(input())
potions = [*map(int,input().split())]
current = 0
for p in potions:
    p = p / 100
    current = 1 - (1 - current) * (1 - p)
    print(current * 100)