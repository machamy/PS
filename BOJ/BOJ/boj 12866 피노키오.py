from collections import defaultdict
N = int(input())
S = input()

cnt = defaultdict(int)

for i in range(N):
    cnt[S[i]] += 1

print(cnt["A"] * cnt["C"] * cnt["G"] * cnt["T"] % 1_000_000_007)

