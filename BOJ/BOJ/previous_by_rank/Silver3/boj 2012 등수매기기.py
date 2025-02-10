import sys
input = sys.stdin.readline

expected = [int(input()) for _ in range(int(input()))]
expected.sort()
ans = 0
for i in range(len(expected)):
    ans += abs(expected[i] - (i + 1))

print(ans)