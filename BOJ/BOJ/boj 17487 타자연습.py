

LEFT = {'Q', 'W', 'E', 'R', 'T', 'Y',\
         'A', 'S', 'D', 'F', 'G',\
           'Z', 'X', 'C', 'V', 'B'}

def is_left(c):
    return c in LEFT
def is_right(c):
    return not is_left(c) and c.isalpha()

def solve(s):
    free_cnt = 0
    left = 0
    right = 0
    for c in s:
        if c == ' ':
            free_cnt += 1
        if c.isupper():
            free_cnt += 1
        C = c.upper()
        if is_left(C):
            left += 1
        if is_right(C):
            right += 1
    # print(free_cnt, left, right)
    while free_cnt > 0:
        if left <= right:
            left += 1
        else:
            right += 1
        free_cnt -= 1

    return left, right

s = input().strip()
left, right = solve(s)

print(left, right)
