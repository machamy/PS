

S,P = map(int,input().split())
temp_string = input()
ACGT = list(map(int,input().split()))

current = [0,0,0,0]
i = 0
for i in range(P):
    c = temp_string[i]
    if c == "A":
        current[0] += 1
    elif c == "C":
        current[1] += 1
    elif c == "G":
        current[2] += 1
    elif c == "T":
        current[3] += 1

def check():
    for i in range(4):
        if current[i] < ACGT[i]:
            return False
    return True

ans = 0
if check():
        current[3] += 1
    
def check():
    for i in range(4):
        if current[i] < ACGT[i]:
            return False
    return True

ans = 0
if check():
    ans += 1

for i in range(P, S):
    c = temp_string[i]
    if c == "A":
        current[0] += 1
    elif c == "C":
        current[1] += 1
    elif c == "G":
        current[2] += 1
    elif c == "T":
        current[3] += 1
    
    c = temp_string[i-P]
    if c == "A":
        current[0] -= 1
    elif c == "C":
        current[1] -= 1
    elif c == "G":
        current[2] -= 1
    elif c == "T":
        current[3] -= 1
    
    if check():
        ans += 1

print(ans)