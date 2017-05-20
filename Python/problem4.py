def palindrome(num):
    rev = 0
    bac = num
    while num != 0:
        rev *= 10
        rev += num % 10
        num = num //10
    return rev == bac

def main():
    largest = -1
    for a in range(999,99,-1):
        for b in range(999,99,-1):
            if palindrome(a*b):
                largest = max(a*b,largest)
    return largest
print(main())
