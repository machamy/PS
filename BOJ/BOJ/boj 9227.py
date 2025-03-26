import sys

xxx = []

while (s := input().rstrip()) != "##":
    xxx.append(s)

while (s := input().rstrip()) != "#":
    
    l = s.split()
    ans = []
    for i in range(len(l)):
        for e in xxx:
            w = l[i]
            a = w.find(e[0])
            b = w.find(e[1])
            if a == -1 or b == -1:
                continue
            if a > b:
                continue
            # print(w)
            w = list(w)
            for j in range(a+1,b):
                w[j] = "*"
            l[i] = "".join(w)
            
    print(*l)
    # print(s)