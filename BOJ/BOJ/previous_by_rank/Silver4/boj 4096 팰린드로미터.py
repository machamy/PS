import sys


def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

while True:
    i = sys.stdin.readline().rstrip()
    if i == "0":
        break
    length = len(i)
    i = int(i)
    cnt = 0
    while True:
        if isPalindrome("%0*d" % (length, i)):
            break
        i += 1
        cnt += 1
    print(cnt)

    


