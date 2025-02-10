import sys
input = sys.stdin.readline

"""
256 = 245 + 2 + 4 + 5
441 = 432 + 4 + 3 + 2

n = 999 + 9+ 9 + 9
n = 99 + 9 + 9
n = 9 + 9
"""
N = input()
n = int(N) 

for i in range(max(0,n - 9 * len(N)),n):
    if i+sum(map(int,str(i))) == int(n):
        print(i)
        break
else:
    print(0)