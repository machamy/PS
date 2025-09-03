import sys
input = sys.stdin.readline

MAX = 12
SUM = 26

def main():
    is_fixed = []
    nums = []

    def parse(nums, is_fixed, s):
        for c in s:
            if c == "x":
                nums.append(0)
                is_fixed.append(False)
            elif c == ".":
                continue
            else:
                nums.append(ord(c) - ord('A') + 1)
                is_fixed.append(True)

    for _ in range(5):
        s = input().rstrip()
        parse(nums, is_fixed, s)

    def ok(nums):
        checklist = [
            [0, 2, 5, 7],
            [1, 2, 3, 4],
            [0, 3, 6, 10],
            [1, 5, 8, 11],
            [7, 8, 9, 10],
            [4, 6, 9, 11],
        ]
        for l in checklist:
            if sum(nums[i] for i in l) != SUM:
                return False
        return True

    used = [False] * 13  # 1~12 사용 여부
    for i in range(MAX):
        if is_fixed[i]:
            used[nums[i]] = True

    def get_next(idx, nums, res):
        if idx == MAX:
            if ok(res):
                return True
            return False

        if is_fixed[idx]:
            res[idx] = nums[idx]
            return get_next(idx + 1, nums, res)

        for i in range(1, 13):
            if used[i]:
                continue
            res[idx] = i
            used[i] = True
            if get_next(idx + 1, nums, res):
                return True
            used[i] = False
            res[idx] = 0
        return False

    def print_result(res):
        ans = [chr(n + ord('A')-1) for n in res]
        print("....{}....".format(ans[0]))
        print(".{}.{}.{}.{}.".format(ans[1], ans[2], ans[3], ans[4]))
        print("..{}...{}..".format(ans[5], ans[6]))
        print(".{}.{}.{}.{}.".format(ans[7], ans[8], ans[9], ans[10]))
        print("....{}....".format(ans[11]))

    res = [0] * MAX
    get_next(0, nums, res)
    print_result(res)

main()
