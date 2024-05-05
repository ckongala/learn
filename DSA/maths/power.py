# Given Two number X, N now we have to find the power x raise to the power of n using BITS

# METHOD -1 ## Best solution for computing power
"""
Time Complexity: O(log(n)),

Space Complexity: O(1).
"""


# if we have to find power under some modulo 'm'
# we have to take 'm' as input and  make this changes res = (res * x) % m and
# similarly we have to make x = (x * x) % m
def power(x, n):
    res = 1
    while n > 0:
        if n & 1:  # n % 2 == 0:
            res = res * x
        x = x * x
        n = n >> 1  # n // 2
    return res


x = int(input("Enter a first number:"))
n = int(input("Enter a second number:"))
print(power(x, n))
