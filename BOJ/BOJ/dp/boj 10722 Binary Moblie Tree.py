import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    sticks = [list(map(int, input().split())) for _ in range(N)]
    parents = [-1] * (N+1)
    local_left_length = [0] * (N+1)
    local_right_length = [0] * (N+1)

    leafs = []
    for i in range(N):
        if sticks[i][0] > 0 and sticks[i][1] > 0:
            leafs.append(sticks[i])
        elif sticks[i][0] < 0:
            parents[-sticks[i][1]] = i + 1
        elif sticks[i][1] < 0:
            parents[-sticks[i][2]] = i + 1
    root = 1    
    # root = -1
    # for i in range(1, N+1):
    #     if parents[i] == -1:
    #         root = i
    #         break
    
    # leftmost = float('inf')
    # rightmost = float('-inf')

    def init_local_length(node):
        length, l,r = sticks[node-1]
        left_weight = l  if l > 0 else init_local_length(-l)
        right_weight = r if r > 0 else init_local_length(-r)
        local_left_length[node] = length * (right_weight) / (left_weight + right_weight)
        local_right_length[node] = length - local_left_length[node]
        return left_weight + right_weight
    
    init_local_length(root)
    # print(f"local_left_length: {local_left_length}")
    # print(f"local_right_length: {local_right_length}")

    def find_ans(node,pos):
        length, l, r = sticks[node-1]
        
        if l < 0:
            find_ans(-l, pos - local_left_length[node])
        else:
            # print(f"{node=} l: {l}, pos: {pos}, local_left_length[node]: {local_left_length[node]}")
            find_ans.leftmost = min(find_ans.leftmost, pos - local_left_length[node])
            find_ans.rightmost = max(find_ans.rightmost, pos + local_right_length[node])
        if r < 0:
            find_ans(-r, pos + local_right_length[node])
        else:
            # print(f"{node=} r: {r}, pos: {pos}, l = {local_left_length[node]} r = {local_right_length[node]}")
            find_ans.leftmost = min(find_ans.leftmost, pos - local_left_length[node])
            find_ans.rightmost = max(find_ans.rightmost, pos + local_right_length[node])

    find_ans.leftmost = float('inf')
    find_ans.rightmost = float('-inf')

    find_ans(root, 0)
    ans = abs(find_ans.rightmost - find_ans.leftmost)
    print(ans)
for _ in range(int(input())):
    solve()