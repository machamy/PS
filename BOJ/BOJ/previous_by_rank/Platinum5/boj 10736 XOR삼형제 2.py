import sys

input = sys.stdin.readline

T = int(input())
MAXIMUM = 101

# a xor b = c 가 되면 안됨...
# 1 2 4 8 끼리는 안겹침
# a ^ b ^ c = 0 이 되면 안됨
# a ^ b ^ (a + b) 는 항상 0
# 001 010 100 -> 111
# 001 011 100 -> 010 100 -> 110
# 001 010 011 -> 011 011 -> 000
# 100 110 -> 010

# 제일 큰 비트 두개는 고정하고, 나머지는 마음대로



def solve():
    N = int(input())
    
    if N == 1:
        print(1)
        print(1)
        return
    if N == 2:
        print(2)
        print(1,2)
        return
    
    largest_bit = 1
    while largest_bit << 1 <= N:
        largest_bit <<= 1
    second_largest_bit = largest_bit >> 1
    
    #print("dbg",second_largest_bit, largest_bit)
    ans = []
    for i in range(second_largest_bit,min(N+1, largest_bit + second_largest_bit)):
        ans.append(i)
        
    print(len(ans))
    print(*ans)
for _ in range(T):
    solve()