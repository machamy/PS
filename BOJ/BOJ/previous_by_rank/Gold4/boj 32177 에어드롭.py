import sys
input = sys.stdin.readline

def union(prnts,a,b):
    a = find(prnts,a)
    b = find(prnts,b)
    if a == b:
        return
    if a < b:
        prnts[b] = a
    else:
        prnts[a] = b
    

def find(prnts,a):
    if prnts[a] != a:
        prnts[a] = find(prnts,prnts[a])
    return prnts[a]

def distance2(a,b,x,y):
    return (a-x)**2 + (b-y)**2

def solve():
    N,K,T = map(int,input().split())
    X,Y,V = map(int,input().split())
    KK = K*K
    infos = [[*map(int,input().split())] for _ in range(N)]
    prnts = [i for i in range(N+1)]
    ans = []

    for j in range(N):
        x,y,v,p = infos[j]
        #print(f"{j=} {distance2(X,Y,x,y)} and {abs(V-v)} ")
        if distance2(X,Y,x,y) <= KK and abs(V-v) <= T:
            union(prnts,0,j+1)
            #print(f"union {0} and {j+1}")
    
    for i in range(N):
        x0,y0,v0,p0 = infos[i]
        for j in range(i+1,N):
            x1,y1,v1,p1 = infos[j]
            if distance2(x0,y0,x1,y1) <= KK and abs(v0-v1) <= T:
                union(prnts,i+1,j+1)
                #print(f"union {i+1} and {j+1}")

    for i in range(N):
        if infos[i][3] == 1 and 0 == find(prnts,i+1):
            ans.append(i+1)
    if ans:
        print(*sorted(ans))   
    else:
        print(0)

solve()

