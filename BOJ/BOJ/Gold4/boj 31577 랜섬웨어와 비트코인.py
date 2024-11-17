N = 20

def next():
    n = 0
    while True:
        n %= N
        n = n + 1
        yield n
g = next()
# test = []
for i in range(15):
    print(*sorted([g.__next__() for _ in range(8)]))
#     test.append(sorted([g.__next__() for _ in range(8)]))

# cnts = [0]*N
# for l in test:
#     for i in range(N):
#         cnts[i] += l.count(i+1)

# print(cnts)