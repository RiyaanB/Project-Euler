n = 600851475143
def prime(num):
    lim = int(num**0.5)+1
    for a in range(2,lim):
        if num % a == 0:
            return False
    return True

largest = -1
lol = True
for a in range(2,n):
    if prime(a):
        while True:
            if n % a == 0:
                n = n//a
                largest = max(a,largest)
                if n == 1:
                    lol = False
            else:
                break
    if not lol:
        break
print(largest)

