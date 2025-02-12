import sys
sys.setrecursionlimit(1<<16)
"""
질문 : 1회
검색 : 1회
"""

#input = sys.stdin.readline
input = open("input.txt","r").readline

def find(prnts,weis, x):
    if prnts[x] == x:
        return x
    p = find(prnts,weis,prnts[x])
    weis[x] += weis[prnts[x]]
    prnts[x] = p
    return prnts[x]

def union(prnts,weis, a, b, w):
    ra = find(prnts,weis,a)
    rb = find(prnts,weis,b)
    if ra==rb :
        return
    prnts[rb] = ra
    weis[rb] = weis[a]-weis[b]+w
    

def solve():
    N,M = map(int,input().split())
    if (N,M) == (0,0):
        return False
    prnts = [i for i in range(N+1)]
    weis = [0 for i in range(N+1)]
    
    for _ in range(M):
        cmd, *args = input().split()
        if cmd == '!':
            a,b,w = map(int,args)
            union(prnts,weis,a,b,w)
        elif cmd =='?':
            a, b = map(int,args)

            if find(prnts,weis,a)!=find(prnts,weis,b):
                print("UNKNOWN")
            else:
                print(weis[b]-weis[a])
    return True
while solve():
    pass