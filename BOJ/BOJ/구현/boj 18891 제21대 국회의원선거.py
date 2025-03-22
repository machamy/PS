import sys
from decimal import Decimal, getcontext
input = sys.stdin.readline
getcontext().prec = 50
# 입력 받기
P,V = map(int,input().split())

MAX_PEOPLE = 300
LOCAL = 253
RATIO = 47

names =[None]
r = [0] * (P + 1)
votes = [0] * (P + 1)
p = [0.0] * (P + 1)
p_low = [0] *(P +1 )


total_r = 0
true_votes = 0
for i in range(1, P + 1):
    name,raw_r,raw_v = input().split()
    names.append(name)
    r[i] = int(raw_r)
    votes[i] = int(raw_v)
    true_votes += votes[i]
    total_r += r[i]

ok_votes = 0
ok_parties = []
R = 253
for i in range(1, P + 1):
    ok_ratio = (votes[i])/(true_votes)
    # print(i,ok_ratio)
    if 0.03 <= (ok_ratio) or r[i] >= 5:
        ok_parties.append(i)
        ok_votes += votes[i]
        R -= r[i]
# 1단계: s 계산
s = [0] * (P + 1)
total_s = 0
for i in ok_parties:
    p[i] = Decimal(votes[i])/Decimal(ok_votes)
    s2 = (MAX_PEOPLE - R) * p[i] - r[i]
    if s2 < 2:
        s[i] = 0
    else:
        s[i] = round(s2/2)
    total_s += s[i]
# print("--- 1 ---")
# for i in ok_parties:
#     print(i,r[i],p[i],s[i])
# 2단계: s 보정 
if total_s < 30:
    remains = []
    tmp_total = 0
    for i in ok_parties:
        tmp = (s[i] + (30 - total_s) * p[i])
        s[i] = int(tmp)
        tmp_total += s[i]
        remains.append((tmp - s[i],i))
    remains.sort(key = lambda x : (-x[0],x[1]))
    while tmp_total < 30:
        for _,idx in remains:
            tmp_total += 1
            s[idx] += 1
            if tmp_total == 30:
                total_s = tmp_total
                break
elif total_s > 30:
    remains = []
    tmp_total = 0
    for i in ok_parties:
        tmp = (30 * s[i]) // (total_s)
        remain_tmp = (30 * s[i]) % (total_s)
        s[i] = int(tmp)
        # print(tmp)
        tmp_total += s[i]
        remains.append((remain_tmp / Decimal(total_s),i))
    # print(remains)
    remains.sort(key = lambda x : (-x[0],x[1]))
    # print(remains)
    while tmp_total < 30:
        for _,idx in remains:
            tmp_total += 1
            s[idx] += 1
            # print(s)
            if tmp_total == 30:
                total_s = tmp_total
                break
    # tmp = remains[:3]
    # t = [x[0] for x in tmp]
    # a,b,c = t
    # print(a<c,c>a,a==c)
# print("--- 2 ---")
# for i in range(1,P+1):
#     print(i,r[i],p[i],s[i])

t = [0 for _ in range(P+1)]
# 3단계 17석 배분
remains = []
tmp_total = 0
for i in ok_parties:
    tmp = 17 * p[i]
    # print(i,p[i],tmp)
    t[i] = int(tmp)
    remains.append((tmp-t[i],i))
    tmp_total += t[i]
# print(remains)
remains.sort(key = lambda x : (-x[0],x[1]))

# print(remains)
while tmp_total < 17:
    for _,idx in remains:
        tmp_total += 1
        t[idx] += 1
        # print(s)
        if tmp_total == 17:
            total_s = tmp_total
            break


# print("--- 3 ---")
# for i in range(1,P+1):
#     print(i,r[i],s[i],t[i],r[i]+s[i]+t[i])

ans = []
for i in range(1,P+1):
    ans.append((names[i],r[i]+s[i]+t[i]))

ans.sort(key = lambda x : (-x[1],x[0]))
for name,num in ans:
    print(name,num)
