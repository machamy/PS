import sys
from collections import deque

input = sys.stdin.readline

D4 = [(0,1),(1,0),(0,-1),(-1,0)]

N,M,K,X = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]


def bfs(i,j,max_diff,visited):

    q = deque()
    visited[i][j] = True
    q.append((i,j))
    cnt = 1
    while q:
        i,j = q.popleft()
        for di,dj in D4:
            ni,nj = i+di,j+dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if visited[ni][nj]:
                continue
            if  max_diff < X - arr[ni][nj]:
                # 인접 노드가 X가 됐음.
                # 차가 설정된 값보다 크면 보정함. 
                visited[ni][nj] = True
                q.append((ni,nj))
                cnt +=1

    return cnt

def test(max_diff):
    total = 0
    visited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] >= X- max_diff:
                # 선명도 최대값은 max_diff
                continue
            if visited[i][j]:
                continue
            
            for di,dj in D4:
                ni,nj = i+di,j+dj
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                if abs(arr[i][j] - arr[ni][nj]) > max_diff:
                    # 설정한 차이값보다 큰경우, 바꿔줌
                    # 더 작은쪽을 올려준다
                    total += bfs(i,j,max_diff,visited)
                    break
    return total
        
l,h = 0, X
while l <= h:
    mid = (l+h) //2
    cnt = test(mid)

    if cnt > K :
        l = mid + 1
    else:
        h = mid -1

print(l)