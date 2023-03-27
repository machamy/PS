def solve(d,m,y):


    yoon = 28
    if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
        yoon = 29
    ans = 30 * sum([4<m,6<m,9<m,11<m]) + 31 * sum([1<m,3<m,5<m,7<m,8<m,10<m]) + (2<m)*yoon + d
    return ans

while True:
    d, m, y = map(int, input().split())
    if m and d and y:
        print(solve(d,m,y))
    else:
        break