s = input()

max_N = 0
if len(s) <= 9:
    max_N = len(s)
else:
    ten_avobe = len(s) - 9
    max_N = 9 + ten_avobe //2

visited = [False] * (max_N + 1)
result = []

def dfs(idx, depth):
    #print(result)
    if depth == max_N:
        print(*result)
        exit()
    if len(result) > max_N:
        return
    remain = max_N - depth
    if remain > len(s) - idx - 1:
        return
    if idx + 1 < len(s):
        if s[idx+1] == '0':
            return
        num = int(s[idx+1])
        if num <= max_N and not visited[num]:
            result.append(num)
            visited[num] = True
            dfs(idx + 1, depth + 1)
            result.pop()
            visited[num] = False
    if idx + 2 < len(s):
        num = int(s[idx+1:idx+3])
        if num <= max_N and not visited[num]:
            result.append(num)
            visited[num] = True
            dfs(idx + 2, depth + 1)
            result.pop()
            visited[num] = False
    

dfs(-1,0)