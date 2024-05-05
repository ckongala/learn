# Given a number, we have see weather given number is a palindrome or not

# METHOD -1
"""
Time Complexity:

Converting an integer to a string: The line b = str(numbers) takes O(log(n)) time, where 'n' is the value of the 
input number. This is because the number of digits in the input number 'n' is log(n) in base 10. Reversing a string: 
The slicing operation b[::-1] creates a reversed copy of the string 'b'. It takes O(n) time, where 'n' is the length 
of the string 'b'. Comparing two strings: The line print(b == b[::-1]) compares the original string 'b' with its 
reversed copy. It takes O(n) time, where 'n' is the length of the string 'b'. Therefore, the overall time complexity 
of the code is O(log(n) + n) = O(n), where 'n' is the number of digits in the input number.

Space Complexity:

numbers: The variable 'numbers' stores the input number as an integer. Its space complexity is O(1). b: The variable 
'b' stores the input number converted to a string. Its space complexity is O(log(n)), where 'n' is the value of the 
input number. This is because the length of the string 'b' is equal to the number of digits in the input number 'n', 
which is log(n) in base 10. Therefore, the overall space complexity of the code is O(log(n)), where 'n' is the value 
of the input number.
"""
numbers = int(input("Enter a number:- "))
b = str(numbers)
print(b == b[::-1])

# METHOD -2  ########BEST APPROACH#############

# """
# Time Complexity:- O(log(n))
# Space Complexity:- O(1)
# """

# n = int(input("Enter a number: "))  ##12321
# reverse = 0
# x = n
#
# while x > 0:
#     ids = x % 10
#     reverse = reverse * 10 + ids
#     x = x // 10
# print(n == reverse)
