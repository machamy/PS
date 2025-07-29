import sys

def restore_record() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    N, K = map(int, data[:2])
    S = data[2].strip()

    W = 2 * K + 1                     # 비트마스크 길이 (diff = -K … +K)
    FULL = (1 << W) - 1

    # ---------- 1) 앞쪽에서부터 가능한 상태 ----------
    pref = [0] * (N + 1)
    pref[0] = 1 << K                  # diff = 0

    for i in range(1, N + 1):
        m = pref[i - 1]
        ch = S[i - 1]
        if ch == 'R':
            nm = m << 1
        elif ch == 'B':
            nm = m >> 1
        else:                         # '?'
            nm = (m << 1) | (m >> 1)
        nm &= FULL                    # 범위 밖 비트 제거

        if i < N:                     # 조기 종료는 금지
            nm &= ~((1 << 0) | (1 << (2 * K)))
        else:                         # 마지막 라운드에서는 꼭 ±K가 되어야 종료
            nm &=  (1 << 0) | (1 << (2 * K))

        pref[i] = nm

    # ---------- 2) 뒤쪽에서부터 가능한 상태 ----------
    suff = [0] * (N + 1)
    suff[N] = (1 << 0) | (1 << (2 * K))   # 경기 종료 상태(±K)

    for j in range(N, 0, -1):
        m = suff[j]
        ch = S[j - 1]
        if ch == 'R':               # 직전 상태는 diff-1
            nm = m >> 1
        elif ch == 'B':             # 직전 상태는 diff+1
            nm = m << 1
        else:                       # '?'  양쪽 다 가능
            nm = (m >> 1) | (m << 1)
        nm &= FULL

        if j - 1 > 0:               # 아직 경기 끝나면 안 됨
            nm &= ~((1 << 0) | (1 << (2 * K)))
        else:                       # start 전 상태 (diff 반드시 0)
            nm &= ~((1 << 0) | (1 << (2 * K)))
        suff[j - 1] = nm

    # ---------- 3) '?'  자리 복구 ----------
    res = list(S)
    for i in range(1, N + 1):
        if res[i - 1] != '?':
            continue
        red  = ((pref[i - 1] << 1) & FULL) & suff[i]
        blue =  (pref[i - 1] >> 1)          & suff[i]

        if red and not blue:
            res[i - 1] = 'R'
        elif blue and not red:
            res[i - 1] = 'B'
        # 둘 다 가능하면 그대로 '?' 유지

    print(''.join(res))

if __name__ == '__main__':
    restore_record()
