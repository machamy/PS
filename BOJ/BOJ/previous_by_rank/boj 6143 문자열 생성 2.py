import sys
from collections import deque
input = sys.stdin.readline
wirte = sys.stdout.write
N = int(input())
chars = [input()[0] for _ in range(N)]
left = 0
right = N-1

ans = deque()

while left < right:
    # 왼쪽문자와 오른쪽 문자중 더 빠른 문자를 선택
    # 선택한 문자를 ans에 추가
    if chars[left] < chars[right]:
        ans.append(chars[left])
        left += 1
    elif chars[left] > chars[right]:
        ans.append(chars[right])
        right -= 1
    else:
        # 만약 두 문자가 같다면
        # 왼쪽과 오른쪽을 비교하며 다른 문자가 나올때까지
        # 비교
        l = left
        r = right
        while l < r and chars[l] == chars[r]:
            l += 1
            r -= 1
        if chars[l] < chars[r]:
            while left < l:
                ans.append(chars[left])
                left += 1
                if chars[left] > chars[right]:
                    break
        else:
            while right > r:
                ans.append(chars[right])
                right -= 1
                if chars[left] < chars[right]:
                    break
if left == right:
    ans.append(chars[left])
cnt = 0
while ans:
    wirte(ans.popleft())
    cnt += 1
    if cnt == 80:
        wirte('\n')
        cnt = 0