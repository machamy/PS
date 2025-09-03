# BOJ 32825  (숫자 할당)
# 입력: A B C D E F G H
# 출력: 경우의 수

import sys
A, B, C, D, E, F, G, H = map(int, sys.stdin.readline().split())

BIT = [1 << i for i in range(13)]          # BIT[x-1] == 1<<(x-1)
nums = range(1, 14)
ans = 0

for d in nums:                             # 열 5 : d + h = D
    h = D - d
    if h < 1 or h > 13 or h == d:          # 1~13, 서로 달라야 함
        continue
    used = BIT[d-1] | BIT[h-1]

    row2_target = E - d                    # a + b + c
    for a in nums:
        if used & BIT[a-1]:
            continue
        used_a = used | BIT[a-1]

        for b in nums:
            if used_a & BIT[b-1]:
                continue
            c = row2_target - a - b
            if (c < 1 or c > 13 or
                c == a or c == b or
                used_a & BIT[c-1]):
                continue
            used_ab = used_a | BIT[b-1] | BIT[c-1]

            row3_target = F - h            # e + f + g
            for e in nums:
                if used_ab & BIT[e-1]:
                    continue
                used_e = used_ab | BIT[e-1]

                for f in nums:
                    if used_e & BIT[f-1]:
                        continue
                    g = row3_target - e - f
                    if (g < 1 or g > 13 or
                        g == e or g == f or
                        used_e & BIT[g-1]):
                        continue
                    used_ef = used_e | BIT[f-1] | BIT[g-1]

                    k = C - (c + g)        # 열 4 : k
                    if k < 1 or k > 13 or used_ef & BIT[k-1]:
                        continue
                    used_k = used_ef | BIT[k-1]

                    need2 = A - (a + e)    # i + l
                    need3 = B - (b + f)    # j + m
                    if not (2 <= need2 <= 26 and 2 <= need3 <= 26):
                        continue

                    # 행 5 조건으로 i 에 무관한 필요 수식 한번 더 걸러줌
                    if H != need2 + need3 - G + k:
                        continue

                    for i in nums:         # 마지막 자유변수 i
                        if used_k & BIT[i-1]:
                            continue
                        l = need2 - i
                        if (l < 1 or l > 13 or l == i or
                            used_k & BIT[l-1]):
                            continue

                        j = G - k - i
                        if (j < 1 or j > 13 or j in (i, l) or
                            used_k & BIT[j-1]):
                            continue

                        m = need3 - j
                        if (m < 1 or m > 13 or
                            m in (i, l, j) or
                            used_k & BIT[m-1]):
                            continue

                        # l + m == H 는 이미 위에서 만족 보증됨
                        ans += 1

print(ans)
