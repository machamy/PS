import sys

input = sys.stdin.readline



"""
0 -> 1 0
1 -> 0 1

.
1
01
1001
01101001
1001011001101001
01101001100101101001011001101001
1001011001101001011010011001011001101001100101101001011001101001
01101001100101101001011001101001100101100110100101101001100101101001011001101001011010011001011001101001100101101001011001101001
1001011001101001011010011001011001101001100101101001011001101001011010011001011010010110011010011001011001101001011010011001011001101001100101101001011001101001100101100110100101101001100101101001011001101001011010011001011001101001100101101001011001101001


1의 개수
0 : 1
1 : 1
2 : 2
3 : 4
4 : 8

01쌍의 개수
0 : 0
1 : 1
2 : 1
3 : 3
4 : 5


00 쌍의 개수
0 : 0
1 : 0
2 : 1
3 : 1
4 : 3
5 : 5
6 : 12


arr[n-2]의 1의 개수 = arr[n-3]의 길이 = 1 << (n-3 -1)
arr[n-1]의 01의 개수 = arr[n-2]의 1의 개수 + arr[n-2]의 00의 개수
arr[n]의 00의 개수 = arr[n-1]의 01의 개수

dp[n] = 1 << (n-3 -1) + dp[n-2]
"""

# def test_print(n):
#     val = len(''.join(map(str, test.strings[n])).split('00'))-1
#     print(val)
#     return val

# def test(n):
#     s = [1]
#     nxt = []
#     test.strings = [None] * (n+1)
#     test.strings[1] = '1'
#     for i in range(2,n):
#         for e in s:
#             if e == 0:
#                 nxt.append(1)
#                 nxt.append(0)
#             else:
#                 nxt.append(0)
#                 nxt.append(1)
#         s = nxt
#         nxt = []
#         test.strings[i] = ''.join(map(str, s))
#         if len(''.join(map(str, test.strings[i])).split('00'))-1 == dp[i]:
#             print(i, len(''.join(map(str, test.strings[i])).split('00'))-1, dp[i])
#         else:
#             break
        

# test(10)
# for l in test.strings:
#     print(l)
# for i in range(1, 1001):
#     if dp[i] != test_print(i):
#         print(i, dp[i], test_print(i))
#         break


# dp = [0] * 1001
# dp[:4] = [0, 0, 1, 1]

# for i in range(4, 1001):
#     dp[i] = (1 << (i-3)) + dp[i-2]

# while True:
#     if (i := input()) != '':
#         n = int(i)
#         print(dp[n])
        
#     else:
#         break
    
dp00 = [0] * 1001
dp11 = [0] * 1001

for i in range(2,1001):
    dp00[i] = dp11[i-1] + dp00[i-1]
    dp11[i] = dp00[i-1] + dp11[i-1]
    if i % 2 == 0:
        dp00[i] += 1
    
    

while True:
    if (i := input()) != '':
        n = int(i)
        print(dp00[n])
        
    else:
        break