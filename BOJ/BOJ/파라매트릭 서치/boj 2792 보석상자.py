import sys
input = sys.stdin.readline


def solve():
    N,M = map(int, input().split())
    gems = [int(input()) for _ in range(M)]
    
    high = max(gems)
    low = 1

    def possible(mid):
        nonlocal gems
        cnt = 0
        for i in range(M):
            # 해당 보석을 mid개씩 나누어줌
            cnt += (gems[i] // mid)
            if gems[i] % mid != 0:
                # 나머지가 있으면 하나 더 추가
                cnt += 1
        return cnt <= N # 보석이 N개 이하로 나누어질 수 있는지 확인

    while low < high:
        mid = (low + high) // 2
        if possible(mid): 
            # 보석을 mid개씩 나누어줄 수 있다면
            # 더 작은 mid를 찾음
            high = mid
        else:
            low = mid + 1

    print(low)


solve()