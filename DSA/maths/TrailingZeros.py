# Given a number, we have to find the count of trailing zeros in factorial of a number.

# METHOD -1
"""
Time Complexity: O(n)
Space Complexity O(1)
"""
# num = int(input("Enter a number:"))
#
#
# def trailing(num):
#     count = 0
#     fact = 1
#     for i in range(2, num + 1):
#         fact = fact * i
#     print(fact)
#     while fact % 10 == 0:
#         count += 1
#         fact = fact // 10
#     return count
#
#
# print(trailing(num))

# METHOD -2  BEST SOLUTION...
"""
Count Number of 2 & 5, These 2 and 5 multiple (2*5) can form a Trailing Zeros.
Shortcut:- Just concentrate on number of '5'. Because '5' are shortage as compare with '2', 
So count of '5' is the solution here!!!

formula:- floor(n/5) + floor(n/25) + floor(n/125) ..........
#STATIC way
# res = num1 // 5 + num1 // 25 + num1 // 125 ......
# print(res)

Time Complexity: O(log(n))
Space Complexity O(1)
"""

num1 = int(input("Enter a number:"))
res = 0
i = 5
while i <= num1:
    res = res + num1 // i
    i = i * 5
print(res)

