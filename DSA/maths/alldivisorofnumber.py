# Given a number, we need to print dividers of the number in sorted order.

# METHOD -1
"""
Time Complexity: O(n),

Space Complexity: O(1).
"""


def diviors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=',')


n = int(input("Enter a number: "))
print(diviors(n))

# METHOD -2 BEST and EFFECTIVE SOLUTION
"""
-> Divisor always appear in pairs.
-> One of the divisors in every pair is smaller than or equal to SQRT(n).
    for a pair (x, y)
     X * Y = n
     let X be the smaller., i.e., x <= y
     x * X <= n
     x < sqrt(n) 

Time Complexity: O(sqrt(n)),

Space Complexity: O(1).     
     

"""


def printdivisors(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
        i += 1
    while i >= 1:
        if n % i == 0:
            print(n / i)
        i -= 1


num = int(input("Enter a number:"))
print(printdivisors(num))
