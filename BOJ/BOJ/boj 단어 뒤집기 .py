
s = input()
st = []

flag = False
for e in s:
    if e == "<":
        while st:
            print(st.pop(), end="")
        st.append(e)
        flag = True
        continue
    if e == ">":
        print(*st, sep="", end="")
        print(">", end="")
        st = []
        flag = False
        continue
    if flag:
        st.append(e)
        continue
    if e == " ":
        while st:
            print(st.pop(), end="")
        print(" ", end="")
    else:
        st.append(e)

while st:
    print(st.pop(), end="")
    