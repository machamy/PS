import sys
from collections import deque
input = sys.stdin.readline

'''
n,m,k
doc

doc의 부분 문자열이 아니면서, 검색창에 들어갈 수 있는 단어는?

'''
sys.setrecursionlimit(5000)

def solve():
    n, m, k = map(int,input().split()) # 길이, 결과 최대길이, 첫 k글자
    doc = input().rstrip()
    alpha = [chr(ord('a') + i) for i in range(k)]
    ans = deque()

    def dfs(depth, string):
        nonlocal m, doc
        if depth == m:
            if string not in doc:
                return string
        else:
            for a in alpha:
                res = dfs(depth + 1, string + a)
                if res is not None:
                    return res
    return dfs(0,'')
#    for a in alpha:
#        res = dfs(1,a)
#        if res is not None:
#            return(res)
        



T = int(input())
for _ in range(T):
    print(solve())