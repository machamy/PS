import sys

input = sys.stdin.readline
"""
사역할 수 없는 경우?

1 2 3 4 4
1 1 1 2

1 2 3 3 4
1 1 1 2

1 2 3 3 4 4
1 1 1 2 3 3
"""

def solve():
    N, M = map(int,input().split())
    
    A = [*map(int,input().split())]
    B = [*map(int,input().split())]

    A.sort()
    B.sort()

    # print(A)
    # print(B)

    i = j = 0
    """
    갈수있는 곳 - 현재까지의 작업 개수 >= 0 이면 작업 가능함.
    => 갈수있는 곳 >= 현재까지 작업개수

    i = 작업 인원
    j = 작업
    """
    for j in range(M): # j = 작업 idx
        # print(f"start work {j}, needs {B[j]}")
        while i < N and B[j] < i + 1:
            j += 1
        while B[j] and i < N:
            #작업가능.
            B[j] -= 1
            i +=1

        if i == N and B[j]:
            #전체 사람 돌았으면... 사역은 서비스 종료다
            return False
            
        # print(f"{j} work OK, ")
    
    return True



if solve():
    print("YES")
else:
    print("NO")