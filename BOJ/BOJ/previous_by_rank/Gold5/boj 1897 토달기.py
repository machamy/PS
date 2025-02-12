import sys
from collections import deque


input = sys.stdin.readline
N, word = input().split()
N = int(N)

dictionary = [[] for _ in range(81)]
words = [input().strip() for _ in range(N)]
start_idx = -1
for idx, w in enumerate(words):
    dictionary[len(w)].append(idx)
    if w == word:
        start_idx = idx
        
def is_possible(origin,target):
    added = False
    for i in range(len(origin)):
        if origin[i] == target[i] and not added:
            continue
        if origin[i] == target[i+1]:
            added = True
            continue
        return False
    return True

ans = start_idx
visited = [False for _ in range(N)]
visited[start_idx] = True
st = deque()
st.append(start_idx)
while st:
    idx = st.pop()
    current_word = words[idx]
    if len(words[ans]) < len(current_word):
        ans = idx
    for candidate_idx in dictionary[len(current_word) + 1]:
        candidate = words[candidate_idx]
        if visited[candidate_idx]:
            continue
        if not is_possible(current_word,candidate):
            continue
        st.append(candidate_idx)
        visited[candidate_idx] = True
print(words[ans])