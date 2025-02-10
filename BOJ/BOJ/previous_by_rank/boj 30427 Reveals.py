import sys

input = sys.stdin.readline


def solve():
    input()
    N = int(input())
    house_people = set([input().strip() for _ in range(N)])
    house_people.add('swi')
    M = int(input())
    seen = set([input().strip() for _ in range(M)])

    if "dongho" in house_people:
        print("dongho")
        return
    not_seen_house = house_people - seen
    if len(not_seen_house) == 1:
        print(not_seen_house.pop())
        return
    if "bumin" in not_seen_house:
        print("bumin")
        return
    if 'cake' in not_seen_house:
        print("cake")
        return
    if 'lawyer' in not_seen_house:
        print("lawyer")
        return
    ans = sorted(not_seen_house)
    if ans[0] == 'swi':
        ans[0] = ans[1]
    print(ans[0])

solve()