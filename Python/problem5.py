def prime(num):
    lim = int(num**0.5)+1
    for a in range(2,lim):
        if num % a == 0:
            return False
    return True
def factors(n):
    fact = []
    for a in range(2,n+1):
        if prime(a):
            while True:
                if n % a == 0:
                    n = n//a
                    fact.append(a)
                    if n == 1:
                        return fact
                else:
                    break
def factorial(n):
    p = 1
    for a in range(1,n+1):
        p *= a
    return p

num = factors(10)
for a in range(2,10):
    lol = factors(a)
    bac = num
    for factor in lol:
        for factor2 in range(len(bac)):
            if factor == bac[factor2]:
                bac.pop(factor2)
                break
        else:
            num.append(factor2)
