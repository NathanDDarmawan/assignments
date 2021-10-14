import math

# numerator input
n = int(input("Enter a numerator: Value must be greater than 0:"))
while n <= 0:
    n = int(input("Please re-enter the numerator. Value must be greater than 0:"))

# denominator input
d = int(input("Enter a denominator: Value must be greater than 0:"))
while d <= 0:
    d = int(input("Please re-enter the denominator. Value must be greater than 0:"))

GCD = int(math.gcd(n, d))

if n < d:  # proper/improper fraction
    print(n, '/', d, "is a proper fraction.")

    if GCD == 1:  # gcd chceck
        print("This proper fraction cannot be reduced any further.")
    else:
        print("This proper fraction can be reduced to:", int(n / GCD), '/', int(d / GCD))

elif n > d:
    print(n, '/', d, "is an improper fraction.")

    if GCD == 1:
        print("This improper fraction cannot be reduced any further.")
    else:
        print("This improper fraction can be reduced to:", int(n / GCD), '/', int(d / GCD))

    wn = n // d  # whole number
    r = n % d  # remainder
    if (r == 0):
        print("The whole number is", wn)
    else:
        print("The mixed number is", wn, "and", r, "/", d)
