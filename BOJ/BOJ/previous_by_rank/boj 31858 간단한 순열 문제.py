N = int(input())
arr = list(map(int, input().split()))

ans = 0
st = []
for i,e in enumerate(arr):
    while st and st[-1] < e:
        # 기억하는 숫자(P_i)가 현재 숫자(P_j)보다 작은경우
        st.pop()
        ans += 1
    if st:
        # 왼쪽에 어떤 숫자가 남은 경우, +1
        ans += 1
    st.append(e)

print(ans)