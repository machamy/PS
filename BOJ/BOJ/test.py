import random

def generate_test_case():
    N = random.randint(1, 50)
    arr = [random.randint(1, 1000) for _ in range(N)]
    return N, arr

N, arr = generate_test_case()
print(N)
print(" ".join(map(str, arr)))