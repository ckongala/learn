# Given a number and find the number of digits in the number.
"""
Time Complicity :- O(log(n))
Space Complicity:- O(1)
"""

Given_number = int(input("Enter a number:"))
Num_Digits = 0
while Given_number > 0:
    Given_number = Given_number // 10
    Num_Digits += 1
print(Num_Digits)
