import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]
K = int(input())

def kmp(word):
    ww = word + word[:-1]
    pattern = word
    pi = [0] * len(pattern)

    # pi 값 계산
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    # print(pi)
    # 패턴 찾기
    cnt = 0
    j = 0
    for i,c in enumerate(ww):
        while j > 0 and c != pattern[j]:
            j = pi[j - 1]
        if c == pattern[j]:
            if j == len(pattern) - 1:
                cnt += 1
                j = pi[j]
            else:
                j += 1
    # print(word, cnt)
    return cnt

ans = 0

# 각 단어 순열
word_list = []
visited = [False] * n
def dfs(word,depth=0):
    if depth == n:
        word_list.append(word)
        return
    for i,w in enumerate(words):
        if not visited[i]:
            visited[i] = True
            dfs(word + w,depth+1)
            visited[i] = False
dfs("")

for word in word_list:
    if kmp(word) == K:
        ans += 1
    
print(ans)    
 