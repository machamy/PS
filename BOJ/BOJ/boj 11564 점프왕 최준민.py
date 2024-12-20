k, a, b = map(int, input().split())

if k == 1:
    print(b-a+1)
else:
    if a == 0:
        print(b//k+1)
    elif a > 0:
        print(b//k - (a-1)//k)
    elif a < 0 and b < 0:
        print(-a//k - (-b-1)//k)
        
    elif a < 0 and b == 0: # a == 0:랑 똑같음
        print(-a//k + 1)
    else:# a < 0 and b > 0
        print( b//k + (-a//k) +1)