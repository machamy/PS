import sys

input = sys.stdin.readline


# 문제
"""
n명의 노움 가족이 단체 사진을 찍기 위해 줄을 서는 것을 좋아합니다.
각 노움은 모자에 1부터 n까지의 숫자가 적혀 있어 고유하게 식별할 수 있습니다.

예를 들어, 5명의 노움이 있다고 가정합시다.
노움들은 다음과 같이 줄을 설 수 있습니다: 1, 3, 4, 2, 5.

이제, 악한 마법사가 줄에서 일부 노움을 제거하고 노움들의 순서를 잊게 만듭니다.
결과는 다음과 같은 부분 수열이 될 수 있습니다: 1, 4, 2.

그는 당신에게 1부터 n까지의 모든 순열을 사전 순서로 정렬했을 때,
남아 있는 부분 수열을 포함하는 첫 번째 순열이 원래의 노움 순서라고 말합니다. 
당신의 임무는 원래의 노움 순서를 찾는 것입니다.
"""


def solve():
    # 풀이
    """
    arr : 일부 순열
    nums : arr에 있는 숫자들
    l : arr에 없는 숫자들(오름차순)

    답은 해당 순열이 포함된 순열중, 최소값

    1. arr을 순회하며 출력한다.
    2. 이때 l에 있는 숫자 중, 더 작은 숫자가 있으면 출력
    """

    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(M)]
    nums = set(arr)
    l = [i for i in range(1, N + 1) if i not in nums]

    idx = 0
    for i in range(M):
        while idx < len(l) and l[idx] < arr[i]:
            print(l[idx])
            idx += 1
        print(arr[i])

    while idx < len(l):
        print(l[idx])
        idx += 1


solve()
