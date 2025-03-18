import sys
sys.setrecursionlimit(10**6)
write = sys.stdout.write
N = int(input())
s = input()
print("#define quadtree_width",N)
print("#define quadtree_height",N)
print("static char quadtree_bits[] = {")

board = [[0 for _ in range(N//8)] for _ in range(N)]


def solve(si,sj,ei,ej):
    if solve.idx == len(s):
        return
    
    # for l in board:
        # print(l)
    # print(f"{(si,sj)=} {(ei,ej)=} {s[solve.idx]}")
    if s[solve.idx] == "Q":
        solve.idx += 1
        solve(si        ,sj         ,(si+ei)//2 ,(sj+ej)//2)
        solve(si        ,(sj+ej)//2+1,(si+ei)//2 ,ej     )
        solve((si+ei)//2+1,sj         ,ei         ,(sj+ej)//2)
        solve((si+ei)//2+1,(sj+ej)//2+1,ei         ,ej     )
        return
    # 해당부분은 해당색
    
    if s[solve.idx] == "W":
        # 흰색
        pass
    else:
        # 검은색
        for i in range(si,ei+1):
            for j in range(sj,ej+1):
                board[i][j//8] += (1 << (j - (j//8) * 8))
    solve.idx += 1
solve.idx = 0
solve(0,0,N-1,N-1)

char = [0,1,2,3,4,5,6,7,8,9,"a",'b','c','d','e','f']
for l in board:
    # print(l)
    for e in l:
        left,right = divmod(e,16)
        # print(left,right)
        write(f"0x{char[left]}{char[right]},")
    write("\n")

print("};")