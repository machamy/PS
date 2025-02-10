import sys

N = int(input())

"""
B0 = 0
B1 = 1

-1 1 1 -1

1 * 1 - 1

Bi = N일때
Bi = B_i-1 * A_(2i-1) - A_(2i)

A는 +1 -1
Bi = B_i-1 - 1 or - B_i-1 + 1
인데.. 마지막에 + 해줘야지?
그럼 앞에는 다 음수로 만들고 마지막에 *-1 + 1 하면 답이네
"""

for i in range(1, N):
    print("1 -1", end=" ")
    
print('-1 1')