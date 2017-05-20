s = 0
def f(a,b):
    if a % 2 == 0:
        global s
        s += a
    if b > 4000000:
        return 0;
    f(b,a+b)
f(1,1)
