ABC = "abcdefghijklmnopqrstuvwxyz"


def solve(S):
    

    alpha = set(S)
    if len(alpha) < 26:
        # 25개보다 작은 경우는 그냥 마지막에 붙여주면 됨
        for c in ABC:
            if c not in alpha:
                print(S+c)
                return
    if S == "zyxwvutsrqponmlkjihgfedcba":
        print(-1)
        return 
    
    """
    1.
    S[-1]의 글자가 S[-2]보다 느린 글자라면 그냥 S[-2]를 pop하면 된다
    ex : wxyz -> wxz -> wxzy
    2. S[-1]의 글자가 S[-2]보다 빠른 글자라면
       S[-1] 빠른 글자가 나올때까지 찾는다.(set에 넣는다)
       빠른글자가 나오면 해당 글자를 pop하고, 마지막에 가장 빠른 글자를 넣는다
    wxzy -> wyxz
    """
    if S[-1] > S[-2]:
        print(S[:24] + S[-1])
        return
    next = S[-1]
    candidates = [next]
    for i in range(24,-1,-1):
        # print(i,S[i],minimum,S[i] > minimum)
        if S[i] > next:
            next = S[i]
            candidates.append(next)
            continue
        candidates.append(S[i])
        candidates.sort()
        print(S[:i] + candidates[candidates.index(S[i])+1])
        return

 
# print(result)
S = input()
solve(S)