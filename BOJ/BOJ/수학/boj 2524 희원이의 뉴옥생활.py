from decimal import Decimal, getcontext
getcontext().prec = 50


Ax,Ay,Bx,By,P,Q,R = map(Decimal, input().split())

for e in [Ax, Ay, Bx, By]:
    if e != int(e):
        assert False, "Input values must be integers."

assert P != 0 and Q != 0, "P or Q is 0"

def dist(x1, y1, x2, y2):
    # print(x1, y1, x2, y2)
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2).sqrt()

def man_dist(x1, y1, x2, y2):
    # print(f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}")
    return abs(x1 - x2) + abs(y1 - y2)
# Px + Qy = R

def get_x(y):
    return (R - Q * y) / P

def get_y(x):
    return (R - P * x) / Q

A = (Ax, Ay)
B = (Bx, By)
if Ax > Bx:
    A, B = B, A
Ax, Ay = A
Bx, By = B

a_candidates = []
b_candidates = []

def is_in_square(x, y):
    # print(f"x: {x}, y: {y}")
    # print(f"Ax: {Ax}, Ay: {Ay}, Bx: {Bx}, By: {By}")
    # print(f"Ax <= x <= Bx: {Ax <= x <= Bx}, Ay <= y <= By: {Ay <= y <= By or By <= y <= Ay}")
    return Ax <= x <= Bx and (Ay <= y <= By or By <= y <= Ay)

if is_in_square(get_x(Ay), Ay):
    a_candidates.append((get_x(Ay), Ay))

if is_in_square(Ax, get_y(Ax)):
    a_candidates.append((Ax, get_y(Ax)))
if is_in_square(get_x(By), By):
    b_candidates.append((get_x(By), By))
if is_in_square(Bx, get_y(Bx)):
    b_candidates.append((Bx, get_y(Bx)))

print(a_candidates)
print(b_candidates)

"""
-0과 0 포함해서 같으면 하나 제거
"""
if len(a_candidates) == 2:
    if a_candidates[0][0] == a_candidates[1][0] \
        and a_candidates[0][1] == a_candidates[1][1]:
        a_candidates.pop()
if len(b_candidates) == 2:
    # print(b_candidates[0][0], b_candidates[1][0])
    # print(f" {b_candidates[0][0]} == {b_candidates[1][0]} : {b_candidates[0][0] == b_candidates[1][0]}")
    if b_candidates[0][0] == b_candidates[1][0] \
        and b_candidates[0][1] == b_candidates[1][1]:
        b_candidates.pop()

if len(a_candidates) == 1 and len(b_candidates) == 1:
    d0 = man_dist(Ax,Ay,a_candidates[0][0], a_candidates[0][1])
    d1 = dist(a_candidates[0][0], a_candidates[0][1], b_candidates[0][0], b_candidates[0][1])
    d2 = man_dist(b_candidates[0][0], b_candidates[0][1], Bx, By)
    res = min(d0 + d1 + d2 , man_dist(Ax, Ay, Bx, By))
    print(f"{res:.13}")
    # print(f"{d0:.10f} {d1:.10f} {d2:.10f}")
else:
    print(man_dist(Ax, Ay, Bx, By))
