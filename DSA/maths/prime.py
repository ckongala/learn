# Given a number, have to check weather it is prime or not

"""
Time Complexity: O(n).

Space Complexity: O(1).
"""
num = int(input("enter a number: "))

# def isprime(n):
#     if n == 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# print(isprime(num))

# METHOD -2 BEST APPROACH....

"""
Time Complexity: O(sqrt(num))..

Space Complexity: O(1). 
"""


def isprime1(num):
    if num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


print(isprime1(num))

"""
Super Efficient!!
Time Complexity:

Space Complexity: O(1). 
"""


def isprime2(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5

    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


print(isprime2(num))
