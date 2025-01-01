import sys

sys.setrecursionlimit(500000)

def sovle():
    N = int(sys.stdin.readline())
    
    # 선물의 합이 소수가 되면 안됨
    
    res = []
    visited = [False] * (N+1)
    flag = False
    
    def is_prime(num, prime_cache={}):
        if num in prime_cache:
            return prime_cache[num]
        if num == 1:
            prime_cache[num] = False
            return False
        if num == 2:
            prime_cache[num] = True
            return True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime_cache[num] = False
                return False
        prime_cache[num] = True
        return True

    
    def dfs(depth,total):
        nonlocal flag
        if is_prime(total) or flag:
            return
        if depth == N:
            print("YES")
            print(*res)
            flag = True
            return
        for j in range(1,N+1):
            if visited[j] is False:
                visited[j] = True
                res.append(j)
                dfs(depth+1,total+j)
                visited[j] = False
                res.pop()
        
    for i in range(1,N+1):
        visited[i] = True
        res = [i]
        dfs(1,total=i)
        visited[i] = False
        if flag:
            break
    if not flag:
        print("NO")
    

sovle()