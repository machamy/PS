import sys
input = sys.stdin.readline

def check(idx1, idx2, original, leet_str, k, leet_dict):

    if idx1 == len(original) and idx2 == len(leet_str): # 둘다 끝에 도달한 경우(동시 도착)
        return True
    elif idx1 == len(original) or idx2 == len(leet_str): # 둘중 하나만 끝인경우는 X
        return False
    
    curr_char = original[idx1]
    
    if curr_char not in leet_dict: # 딕셔너리에 없는 경우
        for i in range(1, k + 1): # 1,2,3 으로 각각 바꾸어 봄
            if idx2 + i > len(leet_str): # 길이 넘어가면 ㅈㅈ
                break
            leet_dict[curr_char] = leet_str[idx2:idx2 + i] # 사전에 리트 추가해보기
            if check(idx1 + 1, idx2 + i, original, leet_str, k, leet_dict): # 다음으로 ㄱㄱ
                return True
            del leet_dict[curr_char]
        return False
    else:   # 딕셔너리에 있는 경우
        mapped = leet_dict[curr_char] # 사전에서 리트 가져옴
        if idx2 + len(mapped) <= len(leet_str) and leet_str[idx2:idx2 + len(mapped)] == mapped:
            # 리트 가져온 다음에 같은지 확인, 같으면 다음으로 ㄱㄱ
            return check(idx1 + 1, idx2 + len(mapped), original, leet_str, k, leet_dict)
        return False

def solve():
        k = int(input())
        original = input().rstrip()
        leet_str = input().rstrip()
        
        leet_dict = {}
        print(1 if check(0, 0, original, leet_str, k, leet_dict) else 0)

T = int(input())
for _ in range(T):
    solve()