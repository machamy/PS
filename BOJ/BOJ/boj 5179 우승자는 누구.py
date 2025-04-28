import sys

input = sys.stdin.readline

def solve():
    # 문제수, 제출수, 참가자수
    M,N,P = map(int, input().split()) 
    failures = [[0 for _ in range(M)] for _ in range(P+1)]
    scores = [[0,0,i+1] for i in range(P)]
    for _ in range(N):
        p,m,t,j = input().split()
        p = int(p)
        m = int(ord(m) - ord('A'))
        if j == '0' and failures[p][m] >= 0:
            failures[p][m] += 1
        else:
            if failures[p][m] == -1:
                continue
            scores[p-1][0] += 1
            scores[p-1][1] += failures[p][m] * 20 + int(t)
            failures[p][m] = -1
    
    scores.sort(key=lambda x: (-x[0], x[1]))
    for solved, time, idx in scores:
        if solved == 0:
            break
        print(idx, solved, time)
    print()
for i in range(int(input())):
    print(f"Data Set {i + 1}:")
    solve()