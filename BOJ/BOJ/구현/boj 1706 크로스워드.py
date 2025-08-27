R,C = map(int,input().split())
world = [input() for _ in range(R)]
words = []

checked_h = [[False for _ in range(C)] for _ in range(R)]
checked_v = [[False for _ in range(C)] for _ in range(R)]
ans = ["z"] * 21

def chk_h(I,J):
    global checked_h
    if checked_h[I][J]:
        return False
    ans = []
    for j in range(J,C):
        if world[i][j] == '#':
            break
        ans.append(world[i][j])
        checked_h[i][j] = True

    if len(ans) > 1:
        return ans
    return False

def chk_v(I,J):
    global checked_v
    if checked_v[I][J]:
        return False
    ans = []
    for i in range(I,R):
        if world[i][j] == '#':
            break
        ans.append(world[i][j])
        checked_v[i][j] = True

    if len(ans) > 1:
        return ans
    return False

for i in range(R):
    for j in range(C):
        a = chk_v(i,j)
        b = chk_h(i,j)

        if a:
            ans = min(ans,a)
        if b:
            ans = min(ans,b)

print(*ans,sep="")
