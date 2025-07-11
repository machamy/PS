import sys
from collections import deque

input = sys.stdin.readline

def main():
    N,M = map(int,input().split())

    cost = 0
    priorities = [0 for _ in range(M+1)]
    q = deque()

    for _ in range(N):
        P,W = map(int,input().split())
        q.append((P,W))
        priorities[P] += 1

    docker = deque()
    current_prioriy = M
    while q:
        # print(cost,q)
        p,w = q.popleft()
        if p != current_prioriy:
            # 돌아가기
            cost += w
            q.append((p,w))
            continue
        priorities[p] -= 1
        cost += w
        temp = deque()
        while docker and docker[-1][0] == p and docker[-1][1] < w:
            # 들어올리기
            cost += docker[-1][1]
            temp.append(docker[-1])
            docker.pop()
        docker.append((p,w))
        while temp:
            docker.append(temp.pop())
            cost += docker[-1][1]


        if priorities[p] == 0:
            current_prioriy -= 1
    print(cost)
main()