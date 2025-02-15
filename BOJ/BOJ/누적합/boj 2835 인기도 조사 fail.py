import sys

input = sys.stdin.readline
write = sys.stdout.write

def parse_input():
    s,e = input().split(" - ")
    start = get_idx(*map(int,s.split(":")))
    end = get_idx(*map(int,e.split(":")))
    return start,end

def get_idx(h,m,s):
    return h*3600+m*60+s



N = int(input())
plus = [0]*(86400 * 2 + 1)
minus = [0]*(86400 * 2 + 1)
arr_sum = [0]*(86400 * 2 + 1)
# print(((86400).bit_length()+1))
for _ in range(N):
    s,e = parse_input()
    if e < s:
        e += 86400
    plus[s] += 1
    minus[e] += 1

current = 0
for i in range(0,len(plus)):
    current += plus[i]
    arr_sum[i] = current + arr_sum[i-1]
    arr_sum -= minus[i]
arr_sum.append(0)
# print(arr)
for _ in range(int(input())):
    s,e = parse_input()
    total = 0
    delta = 1
    if e < s:
        total = arr_sum[e+86400] - arr_sum[s-1] + arr_sum[e]
        delta = e + 86400 - s + 1
        # print(f"{arr[e+86400]} - {arr[s-1]} + {arr[e]}")
    else:
        total = arr_sum[e] - arr_sum[s-1]
        if e + 86400 < len(plus):
            total += arr_sum[e+86400] - arr_sum[s+86400-1]
        delta = e-s + 1
        # print(f"{arr[e]} - {arr[s-1]}")
    write(f"{total/(delta):.10f}\n")