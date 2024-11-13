import sys
input = sys.stdin.readline


def get(idx):
    print(f"? {idx}")
    sys.stdout.flush()
    return input()
def ans(idx):
    print(f"! {idx}")
    sys.stdout.flush()
    return input()

def solve():
    n = int(input())
    
    i = 2
    while i < n:
        a = get(i)
        if i == 1:
            ans(i)
            return
        i += 1

solve()