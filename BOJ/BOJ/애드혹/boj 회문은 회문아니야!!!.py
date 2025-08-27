import sys

input = sys.stdin.readline

"""
ABBAC



"""

S = input().rstrip()

is_pelindrome = True
for i in range(len(S)//2):
    if S[i] != S[-i-1]:
        is_pelindrome = False
        break

if len(set(S)) == 1:
    print(-1)
elif is_pelindrome:
    print(len(S)-1)
else:
    print(len(S))
    

