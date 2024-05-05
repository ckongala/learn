# Given a number, we have to find the factorial of the number.

# METHOD -1 # BEST SOLUTION...
"""
Time Complexity: O(n)
Space Complexity O(1)
"""
number = int(input("Enter a number: "))
fact = 1
for i in range(2, number + 1):
    fact = fact * i

print(fact)

# METHOD -2
# Recursive way

"""
Time Complexity: O(n)
Space Complexity O(n)
"""
# numb = int(input("Enter a number:"))
#
#
# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num - 1)
#
#
# print(factorial(numb))
