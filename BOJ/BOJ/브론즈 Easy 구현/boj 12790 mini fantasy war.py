T =int(input())

for _ in range(T):
    HP,MP,ATK,DEF,dhp,dmp,datk,ddef = map(int,input().split())
    ans = max(1,HP+dhp) + 5* max(1,MP+dmp) + 2*max(0,ATK + datk) + 2*(DEF + ddef)
    print(ans)
