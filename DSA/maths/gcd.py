# # Given two number, find the GCD
#
# """
# Euclidean Algorithm
# Time Complexity:
#
# Taking input: The lines a = int(input("Enter a number1:")) and b = int(input("Enter a number2:")) take constant time,
# O(1). The while loop: The loop runs until 'a' and 'b' become equal. In each iteration, either a or b is reduced by
# the value of the other variable (a = a - b or b = b - a). The subtraction operation takes constant time,
# O(1). The number of iterations in the loop depends on the GCD (Greatest Common Divisor) of the two input numbers 'a'
# and 'b'. The Euclidean algorithm is used to find the GCD, and its time complexity is O(log(min(a, b))). The
# worst-case occurs when the two numbers are consecutive Fibonacci numbers. However, for practical purposes,
# the GCD is found quickly, so the overall time complexity is considered to be O(log(min(a, b))). Therefore,
# the overall time complexity of the code is O(log(min(a, b))).
#
# Space Complexity:
#
# a and b: These variables store integer values and occupy a constant amount of memory, O(1). Therefore, the overall
# space complexity of the code is O(1), as it uses only a constant amount of additional memory, regardless of the input
# numbers 'a' and 'b'."""
#
# a = int(input("Enter a number1:"))
# b = int(input("Enter a number2:"))
#
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print(a)
#
# """
# OPTIMISED EUCLIDEAN ALGORITHM
#
# Time Complexity: O(log(min(a, b)
#
# Space Complexity: O(log(min(a, b)
#
# """
#
#
# # def gcd(a, b):
# #     if b == 0:
# #         return a
# #     return gcd(b, a % b)
# #
# #
# # print(gcd(a, b))

