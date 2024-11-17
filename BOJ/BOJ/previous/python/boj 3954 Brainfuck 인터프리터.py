import sys
input = sys.stdin.readline

MaxSize = 256
MaxRecursion = 50_000_000

def solve():
    arrSize, codeSize, inputSize = map(int,input().split())
    p = 0
    arr = [0] * arrSize
    code = input().rstrip()
    data = input().rstrip()

    count = 0
    idx = 0
    dataidx = 0
    stack = []
    while idx < codeSize:
        cmd = code[idx]
        match cmd:
            case "+":
                arr[p] = (arr[p] + 1) % MaxSize
            case "-":
                arr[p] = (arr[p] - 1)
                if arr[p] < 0:
                    arr[p] = MaxSize - 1
            case "<":
                p -= 1
                if p < 0:
                    p = arrSize -1
            case ">":
                p += 1
                if p >= arrSize:
                    p = 0
            case "[":
                stack.append(idx)
                if arr[p] == 0:
                    tmp = len(stack) # 시작시 스택의 크기
                    while len(stack) >= tmp: # 더 작아질 경우 루프 끝
                        idx += 1
                        if code[idx] == "[":
                            stack.append(idx)
                        elif code[idx] == "]":
                            stack.pop()
            case "]":
                pair = stack.pop()
                if arr[p] != 0:
                    idx = pair - 1
            case ".":
                pass
                # print(arr[p])
            case ",":
                if dataidx >= inputSize:
                    arr[p] = 255
                else:
                    arr[p] = ord(data[dataidx])
                    dataidx += 1
        count += 1
        idx += 1
        if count > MaxRecursion:
            break    
    else:
        print("Terminates")
        return
    count = 0
    m = 10000
    M = -1
    print("@@@@@@@",idx,code[idx],code[idx+1])
    while idx < codeSize:
        cmd = code[idx]
        match cmd:
            case "+":
                arr[p] = (arr[p] + 1) % MaxSize
            case "-":
                arr[p] = (arr[p] - 1)
                if arr[p] < 0:
                    arr[p] = MaxSize - 1
            case "<":
                p -= 1
                if p < 0:
                    p = arrSize -1
            case ">":
                p += 1
                if p >= arrSize:
                    p = 0
            case "[":
                stack.append(idx)
                if arr[p] == 0:
                    tmp = len(stack) # 시작시 스택의 크기
                    while len(stack) >= tmp: # 더 작아질 경우 루프 끝
                        idx += 1
                        if code[idx] == "[":
                            stack.append(idx)
                        elif code[idx] == "]":
                            stack.pop()
            case "]":
                pair = stack.pop()
                if arr[p] != 0:
                    m = min(m,pair)
                    M = max(M,idx)
                    idx = pair - 1
            case ".":
                pass
                # print(arr[p])
            case ",":
                if dataidx >= inputSize:
                    arr[p] = 255
                else:
                    arr[p] = ord(data[dataidx])
                    dataidx += 1
        count += 1
        idx += 1
        if count >= MaxRecursion:
            print("Loop",m,M)
            break 
    return

for _ in range(int(input())):
    solve()