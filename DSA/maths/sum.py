# Printing the sum of the given numbers.
"""
method - 1
we have brackets here, so it have top priority,
multiplication and division both have same precedence, when two
things have same precedence associativity is Consider and associativity
of multi and division is left to right.

Time Complicity is O(1)
Space Complicity is O(1)
"""
Given_number = int(input("Enter a number:"))
print((Given_number * (Given_number + 1)) / 2)

# """
# method - 2
#
# Time Complicity is O(n)  # Here 'n' is size of input
# Space Complicity is O(1)
# """
# number = int(input("Enter a number: "))
# count = 0
# for i in range(number+1):
#     count += i
# print(count)
