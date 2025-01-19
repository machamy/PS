import sys
input = sys.stdin.readline

def solve():
    Q = int(input())
    arr = []
    mid = 0
    left_sum = 0
    right_sum = 0
    for _ in range(Q):
        cmds = input().split()
        if cmds[0] == '1':
            i = int(cmds[1])
            arr.append(i)
            if len(arr) % 2 == 0:
                mid += 1
                left_sum += arr[mid-1]
                right_sum -= arr[mid-1]
            right_sum += i
        elif cmds[0] == '2':
            # print(f"left {arr[:mid]} \n right {arr[mid:]}")
            # print(f"left_sum {left_sum} right_sum {right_sum}")
            if left_sum <= right_sum:
                print(left_sum)
                arr = arr[mid:]
            else:
                print(right_sum)
                arr = arr[:mid]
            mid = len(arr) // 2
            left_sum = sum(arr[:mid])
            right_sum = sum(arr[mid:])
        
    print(*arr)


solve()