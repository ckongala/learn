# Given two number, we have to find the LCM

"""
NAVIE APPROACH
Time Complexity: O(a * b).

Space Complexity: O(1).

"""
a = int(input("Enter a number1:"))
b = int(input("Enter a number2:"))


def lcm(a, b):
    res = max(a, b)
    while True:
        if res % a == 0 and res % b == 0:
            return res
        res += 1
    return res


print(lcm(a, b))


"""
Efficient way to solve this problem
formula:- a*b = gcd(a,b) * lcm(a,b)
"""

