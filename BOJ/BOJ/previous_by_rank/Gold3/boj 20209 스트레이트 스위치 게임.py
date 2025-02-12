from collections import deque

N, K = map(int, input().split())
nums = [*map(int, input().split())]
graph = []
visited = set()

for _ in range(K):
    graph.append([*map(int, input().split())][1:])


def isOk(L):
    for i in range(1, len(L)):
        if L[i] != L[i - 1]:
            return False
    return True


def click(switch, L):
    for e in graph[switch]:
        L[e - 1] = (L[e - 1] + (switch + 1)) % 5


q = deque()
q.append((0, nums))
while q:
    cnt, L = q.popleft()

    if isOk(L):
        print(cnt)
        break

    for i in range(K):
        tmp = L[:]
        click(i, tmp)

        if tuple(tmp) not in visited:
            visited.add(tuple(tmp))
            q.append((cnt + 1, tmp))
else:
    print(-1)
