from collections import deque
N,m = map(int,input().split())
ans = 0
'''
각 버튼 두번 누르는것은 같은 행동 -> 0번 혹은 1번만 누르게

000
100
010
101

'''
t1 = N
t2 = N // 2
t3 = N // 2 + N % 2
t4 = (N - 1) // 3 + 1

# 아무 버튼도 누르지 않는 경우
ans += 1 

# 동작 1 : 모든 버튼
if(t1 <= m):
    ans += 1

# 동작 2 : 짝수 버튼
if(t2 <= m and N > 1): # N이 1보다 클 때만
    ans += 1

# 동작 3 : 홀수 버튼
if(t3 <= m and N > 1): # N이 1보다 클 때만, 1,2이면 모든버튼과 같은 상태
    ans += 1

# 동작 4 : 3k+1 버튼
if(t4 <= m and N > 2): # N이 2보다 클 때만, 1이면 모든버튼, 2이면 홀수버튼과 같은 상태
    ans += 1

# 동작 2 + 4 : 짝수 버튼 + 3k+1 버튼
if(t2 + t4 <= m and N >= 3): 
    ans += 1

# 동작 3 + 4 : 홀수 버튼 + 3k+1 버튼
if(t3 + t4 <= m and N >= 3): 
    ans += 1

# 동작 1 + 4 : 모든 버튼 + 3k+1 버튼
if(t1 + t4 <= m and N >= 3):
    ans += 1

print(ans)