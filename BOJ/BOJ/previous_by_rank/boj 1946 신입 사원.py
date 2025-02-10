import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    people = [list(map(int, input().split())) for _ in range(n)]
    people.sort(key=lambda x: x[0])
    
    min_rank = n+1
    cnt = 0
    for i in range(n):
        if people[i][1] < min_rank:
            cnt += 1
            min_rank = people[i][1]
            
    print(cnt)

    

T = int(input())
for _ in range(T):
    solve()