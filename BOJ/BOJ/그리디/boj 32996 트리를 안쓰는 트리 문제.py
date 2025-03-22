

"""
12/1/2

1234123412341234
1234/1/2341/2/3412/3/4

1234
2341
3412
4321

1 4 1 1
6 9 2 1
11 14 3 1
15 15 1 1

1234
2341
2421
4

1212

12


"""


def solve():
    N = int(input())

    remains = []
    current_idx = 0
    start_color = 1
    ans = []
    while current_idx < N*N:
        current_color = current_idx % N + 1
        # print(current_i4dx,start_color,current_color)

        end = current_idx + N
        if end < N*N:
            ans.append((current_idx+1,end,start_color,1))
            remains.append((end,current_color))
            current_idx += N + 1
            start_color += 1
        else:
            ans.append((current_idx+1,current_idx+1,current_color,1))
            for i,e in enumerate(remains):
                idx,color = e
                ans.append((idx+1,idx+1,N,color+1))
            break
    print(len(ans))
    for e in ans:
        print(*e)

solve()