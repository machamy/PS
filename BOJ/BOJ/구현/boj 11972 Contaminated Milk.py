import sys

input = sys.stdin.readline

def solve():
    N,M,D,S = map(int,input().split())

    #p, m, t
    drinks = [map(int,input().split()) for _ in range(D)]
    infected = [list(map(int,input().split())) for _ in range(S)]

    data = [[] for _ in range(N)]
    milk = [0] * M
    for p,m,t in drinks:
        data[p-1].append((t,m))
        
    for pi,ti in infected:
        for td,md in data[pi-1]:
            # 해당 사람이 마신 우유 점검
            if td < ti:
                milk[md-1] += 1 # 위험한 우유를 마신 위험군 +1
    
    ans = 0
    for i in range(M):
        if milk[i] < S:
            # 해당 우유는 위험하지 않음
            continue
        # 모든 우유에 대하여
        tmp = 0
        for person in data:
            for t,m in person:
                if m == i+1: # 해당 우유를 마신 사람이 있다면
                    tmp += 1 # 사람수 +1
                    break
        ans = max(ans,tmp)
    print(ans)

solve()