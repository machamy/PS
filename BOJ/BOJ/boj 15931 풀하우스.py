def solve():
    N = int(input())
    R = 52 - N

    M = 0
    m = 0
    if R <= 26:
        m = 0
    elif R <= 38:
        m = int((R-26) / 2 + 0.5)
    elif R <= 40: # 7 x, 7 7
        m = 6
    elif R <= 42: #
        m = 7
    else:
        m = 8
    cards = [0] * 14
    types = [0] * 5
    if R < 5:
        M = 0
    elif R <= 40:
        M = R // 5
    else:
        M = 8

    print(m,M)


solve()