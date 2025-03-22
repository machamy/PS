def solve():
    n,k = map(int,input().split())
    if n == 1:
        if k:
            print("NO")
            return
        print("YES")
        print(".")
        return
    if n == 2:
        if k == 0:
            print("YES")
            print("..")
            print("..")
        elif k == 1:
            print("YES")
            print("#.")
            print("..")
        else:
            print("NO")
        return
    if k > (n-1) * n:
        print("NO")
        return
    print("YES")

    for j in range(n-1):
        if k:
            print("#",end="")
            k-=1
        else:
            print(".",end="")
    print(".",end="")
    print()
    for i in range(1,n-1):
        for j in range(n):
            if i == j:
                print(".",end="")
            elif k:
                print("#",end="")
                k-=1
            else:
                print(".",end="")
        print()
    print(".",end="")
    for j in range(n-1):
        if k:
            print("#",end="")
            k-=1
        else:
            print(".",end="")
    print()


solve()
