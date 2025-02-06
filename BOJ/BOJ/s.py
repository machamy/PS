

A,B = [],[]
print(id(A),id(B))
def f():
    global A,B
    A,B = B,A
f()
print(id(A),id(B))