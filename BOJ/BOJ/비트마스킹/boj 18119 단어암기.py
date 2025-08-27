import sys

input = sys.stdin.readline

N, M = map(int, input().split())
strings = [input().rstrip() for _ in range(N)]
string_flags = [0] * N
memory = 0
for i in range(N):
    for char in strings[i]:
        string_flags[i] |= (1 << (ord(char) - ord('a')))
    memory |= string_flags[i]

for _ in range(M):
    cmd, x = input().split()
    if x not in "aeiou":
        x = ord(x) - ord('a')
        if cmd == '2':
            memory |= (1 << x)
        else:
            memory &= ~(1 << x)
    # print(bin(memory))
    count = 0
    for i in range(N):
        if (string_flags[i] & memory) == string_flags[i]:
            count += 1
    print(count)