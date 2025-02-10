import sys 

N, S, E = map(int,input().split())

# S를 트리의 루트로 가정.
# dfs로 경로 탐색.
# 1턴부터 시작
# 짝수 턴에 갈 수 있는 길이 하나 뿐이면 선공, 아니면 후공

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

st = [S]
prev = [None for _ in range(N+1)]
prev[S] = -1
path_cnt = [0 for _ in range(N+1)]
while st:
    current = st.pop()
    if current == E:
        break
    for nxt in tree[current]:
        if prev[nxt] is not None:
            continue
        st.append(nxt)
        prev[nxt] = current
        path_cnt[current] += 1
        # print(f"{current} -> {nxt}")

def get_path():
    res = []
    c = E
    while c != S:
        res.append(c)
        c = prev[c]
    return res

path_without_S = list(reversed(get_path()))

# for i,e in enumerate(path_without_S):
#     print(f"{i} : {e}")
#     print(f"cnt : {path_cnt[e]}")
for n in path_without_S[:-1:2]:
    # print(f"checked {n}")
    if path_cnt[n] > 1:
        print("Second")
        break
else:
    print("First")