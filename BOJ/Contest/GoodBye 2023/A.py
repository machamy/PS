import sys
input = sys.stdin.readline
print = sys.stdout.write

for i in range(int(input())):
    n = int(input())
    m = n % 100
    n = (n+1)

    if(n%m == 0):
        print("Good\n")
    else:
        print("Bye\n")
