import decimal

decimal.getcontext().prec = 1000

def cube_root(n):
    x = decimal.Decimal(n)
    pow = decimal.Decimal("1")/decimal.Decimal("3")
    res = x**pow
    res = round(res,500)
    res = res.quantize(decimal.Decimal(".0000000001"),rounding=decimal.ROUND_DOWN)
    return res

# print(cube_root(int('98'*75)))
# print(cube_root(int('9'*150)))
for _ in range(int(input())):
    n = int(input())

    print(cube_root(n))

    