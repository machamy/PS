import sys
import bisect

input = sys.stdin.readline

N,M = map(int,input().split())
B = list(map(int,input().split()))
B.sort()
asteroids = [list(map(int,input().split())) for _ in range(M)]

ans = 0
for i in range(M):
    idx = bisect.bisect_left(B,asteroids[i][0])
    l,r = idx-1,idx
    min_dist = float("inf")
    if l >= 0:
        min_dist = min(min_dist,abs(asteroids[i][0]-B[l]))
        print(f"{asteroids[i][0]= }l: {l}, min_dist: {min_dist}")
    if r < N:
        min_dist = min(min_dist,abs(asteroids[i][0]-B[r]))
        print(f"{asteroids[i][0]= }r: {r}, min_dist: {min_dist}")
    ans = max(ans,min_dist*asteroids[i][1])
print(ans)