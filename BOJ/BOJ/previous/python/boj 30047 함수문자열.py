


def solve():
    f = input()
    s = []
    for c in reversed(f):
        if c == "x":
            s.append(0)
        elif c == "g":
            if not s :
                print(-1)
                return
            s.append(s.pop()+1)
        elif c == "f":
            if len(s) < 2:
                print(-1)
                return
            s.append(min(s.pop(),s.pop()))
    if len(s) == 1:
        print(s.pop())
    else:
        print(-1)

solve()