import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    adjc_list = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int, input().split())
        adjc_list[a].append(b)
        adjc_list[b].append(a)

    st = [1]
    cnt = 0
    visited = [False for _ in range(N+1)]
    visited[1] = True
    while st:
        cur = st.pop()
        for nxt in adjc_list[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                cnt += 1
                st.append(nxt)
    print(cnt)