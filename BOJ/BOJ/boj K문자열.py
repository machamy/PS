import sys

input = sys.stdin.readline

def count_bit(n):
    cnt = 0
    # print(bin(n))
    while n:
        if n & 1:
            cnt += 1
        n >>= 1

    # print(cnt)//
    return cnt
    
def main():
    N,K = map(int,input().split())

    cnts = [0 for _ in range(1 << 10)]

    for _ in range(N):
        s = input().rstrip()
        flag = 0
        for c in s:
            flag |= 1 << (ord(c) - ord('0'))
        
        cnts[flag] += 1
    ans = 0
    for i in range(1 << 10):
        for j in range(i, 1 << 10):
            if cnts[i] == 0 or cnts[j] == 0:
                continue
            
            res = i | j
            if count_bit(res) != K:
                continue
            
            if i == j:
                # 자기 자신과 되는경우 제외해야함.
                ans += (cnts[i] * (cnts[j] - 1) // 2)
            else:
                ans += cnts[i] * cnts[j]
            # print(ans, bin(i), bin(j))

    print(ans)

main()