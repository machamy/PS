import heapq

L = int(input())
S = list(map(int, input().split()))
n = int(input())
S.sort()


"""
[1,5]
12 123 1234 12345
23 234 2345
34 345
45
2~3 2~4 2~5 
3~4 3~5 
4~5

1 : 4
2 : 7 = 4 + 3
3 : 8 = 3 + 3 + 2
4 : 7 = 2 + 2 + 2 + 1
5 : 4 = 1 + 1 + 1 + 1
1 : 1,5
2 : 2,4
3 : 3,3
4 : 4,2
5 : 5,1
"""
def get_priority(n,a,b):
    left = n - a
    right = b - n
    return left * right - 1

hq = []
S = [0] + S
for s in S[1:]:
    heapq.heappush(hq, (0, s))

for i in range(0,len(S)-1):
    a = S[i]
    b = S[i+1]
    if b - a - 1 >= n:
        for d in range(1, n // 2 + 2):
            heapq.heappush(hq, (get_priority(j:=a + d,a,b), j))
            heapq.heappush(hq, (get_priority(j:=b - d,a,b), j))
    else:
        for j in range(a+1, b):
            heapq.heappush(hq, (get_priority(j,a,b), j))
ans = []
for i in range(n):
    if hq:
        ans.append(heapq.heappop(hq)[1])
    else:
        ans.append(S[-1]+1)
        S[-1] += 1
print(*ans)