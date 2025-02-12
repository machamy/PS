import sys

input = sys.stdin.readline

T = int(input())

# AAAA 의 경우는 0+0임.
# BAAA 의 경우는 0+1임.
# AAAB 의 경우는 1+1임

def solve():
    name = input().strip()
    
    
    change_count = 0
    
    for c in name:
        pos = ord(c) - ord('A')
        change_count += min(pos, 26 - pos)
    if change_count == 0:
        print(0)
        return
    # 시작에서 어떤점을 찍고, 돌아올 것인지 이어갈 것인지 확인
    # 가장 긴 A는 스킵하면 됨... 어떻게?
    # 시작과 포함된 가장긴 A는 스킵못함. 쪼개야함
    # AAAABAAAAAAA : 오른쪽 4번. 끝
    # AAAABAAAAAAAB : 왼 1 오 5
    # AAAABAB : 왼 3 오 0
    L = len(name)
    min_move = len(name)
    
    def chk(i):
        nonlocal min_move
        # 다음 목표 지점
        nxt_char = i + 1
        while nxt_char < L and name[nxt_char] == 'A':
            nxt_char += 1
        
        # 여기까지 찍고, 돌아가서 다음 목표지점 찍기
        go_back = i * 2 + L - nxt_char
        # 해당 목표지점까지 찍고, 여기로 돌아오기
        return_back = i + (L - nxt_char) * 2
        # print(i,nxt_char,go_back, return_back)
        min_move = min(min_move, go_back, return_back)
        
    chk(0)
    for i in range(1,L):
        if name[i] != 'A':
            chk(i)
        

    print(change_count + min_move)
    

for _ in range(T):
    solve() 