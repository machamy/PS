import sys
from heapq import heappop,heappush

input = sys.stdin.readline


def main():
    V,E = map(int,input().split())
    adj = [[] for _ in range(V+2)]

    for _ in range(E):
        u,v,w = map(int,input().split())
        adj[u].append((v,w))
        adj[v].append((u,w))
    
    is_house = [True for _ in range(V+1)]

    M,x = map(int,input().split())
    mcs = list(map(int,input().split()))
    for e in mcs:
        adj[-1].append((e,0))
        is_house[e] = False

    S,y = map(int,input().split())
    sts = list(map(int,input().split()))
    for e in sts:
        adj[0].append((e,0))
        is_house[e] = False

    def find_dists(start,lim):
        q = [(0,start)]
        dist = [float('inf') for _ in range(V+2)]
        dist[start] = 0
        while q:
            cost, node = heappop(q)
            if dist[node] < cost:
                continue

            for nxt, nxt_cost in adj[node]:
                new_cost = cost + nxt_cost
                if new_cost < dist[nxt]:
                    
                    if new_cost <= lim:

                        heappush(q,(new_cost, nxt))
                        dist[nxt] = new_cost
                
        return dist

    ans = float('inf')
    mc_dist = find_dists(-1,x)
    st_dist = find_dists(0,y)
    for i in range(1,V+1):
        if is_house[i]:
            ans = min(ans,mc_dist[i]+st_dist[i])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
main()