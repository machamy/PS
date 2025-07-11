import sys

input = sys.stdin.readline

def main():
    N = int(input()) # 1~300'000
    clicks = [list(map(int, input().split())) + [i+1] for i in range(N)]
    clicks.sort()

    """
    클릭의 시작을 기준으로 정렬
    클릭의 시작이 이전 끝점보다 작거나 같으면 같은 그룹으로 묶는다
    그룹의 최대 끝점을 갱신한다

    만약 클릭의 시작이 이전 끝점보다 크면 새로운 그룹을 시작한다.
    시작하기 전에 최대값과 비교해 갱신.
    """

    ans_group = None # [최대 끝점, 클릭 리스트]
    current_group = [-1,[]] # [최대 끝점, 클릭 리스트]

    for start, end, i in clicks:

        if start < current_group[0]:
            # 현재 그룹에 추가
            current_group[0] = max(current_group[0], end)
            current_group[1].append(i)
        else:
            # 새로운 그룹 시작
            if ans_group is None:
                ans_group = current_group[1]
            else:
                if len(ans_group) < len(current_group[1]):
                    ans_group = current_group[1]
            current_group = [end, [i]]
    if ans_group is None:
        ans_group = current_group[1]
    else:
        if len(ans_group) < len(current_group[1]):
            ans_group = current_group[1]

    print(len(ans_group))
    print(*ans_group)

main()