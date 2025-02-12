import sys

input = sys.stdin.readline

N,M = map(int, input().split())
# N : 유용한 물건 수
# M : 스카우트 대원 수

sizes = list(map(int, input().split()))
amount = len(sizes)
ans = 0
sizes.sort()
def is_possible(size):
    l,r = 0,amount-1
    cnt = 0
    while l<=r:
        mid = (l+r)//2
        if sizes[l] + sizes[r] <= size:
            l += 1
        r -= 1
        cnt += 1

        if cnt > M:
            return False
    return True

l,r = sizes[-1],sum(sizes)
while l <= r:
    mid = (l+r)//2
    if is_possible(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans) 