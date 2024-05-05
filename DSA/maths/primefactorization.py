# Given  a number, we have to find the Prime Factorization ...

"""
Time Complexity: O(n * sqrt(n)),

Space Complexity: O(1).
"""


def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def printprimefactors(n):
    for i in range(2, n + 1):
        if isprime(i):
            x = i
            while n % x == 0:
                print(i)
                x = x * i


n = int(input("Enter a number:"))
print(printprimefactors(n))
