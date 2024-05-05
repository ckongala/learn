# Working of recursion:- It is same as iteration Application of recursion:-
# >>Many algorithm techniques are based on it
# 1.DP, 2.Backtracking 3.Divide and Conquer(Binary Search, Quick Sort, Merge sort).
# >> Many problems inherently recursive.
# 1.Tower of hanoi,
# 2.DFS based traversals(DFS of Graph and Inorder/Preorder/Postorder traversal of tree)
######################################################################################################################

# Factorial using Recursion...
"""
Time Complexity of the code is O(n),
Space Complexity is also O(n),  # where n is the input to the fact function.
"""


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


print(fact(4))

######################################################################################################################

# Fibonacci series using Recursion...
"""
Time Complexity of the code is approximately O(φ^n)
Space Complexity is O(n)
"""


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(3))

######################################################################################################################


# Tail Recursion:- If the function does not do anything after the last recursive call.
"""
Time Complexity of the code is O(n), 
Space Complexity is O(n),  # where n is the input to the function
"""


def fun(n):
    if n <= 0:
        return
    print(n, end='')
    fun(n - 1)


print(fun(4))

######################################################################################################################


# Binary representation of the number using recursion.
"""
Time Complexity of the code is O(log n),
Space Complexity is also O(log n),  # where n is the input number to the function.
"""


def binary(n):
    if n == 0:
        return
    binary(n // 2)
    print(n % 2)


binary(10)

######################################################################################################################
# sum of the digits using recursion.
"""
Time Complexity :- O(log n)
Space Complexity :- O(log n)
"""


def su(n):
    if n < 10:
        return n
    k = n % 10
    return k + su(n // 10)


print(su(252))

######################################################################################################################

# Palindrome using recursion.

"""
Time Complexity :- O(N)
Space Complexity :- O(N)
"""


def pal(s, start, end):
    if start >= end:
        return True

    return s[start] == s[end] and pal(s, start + 1, end - 1)


s = 'abuzz'
start = 0
end = len(s) - 1
print(pal(s, start, end))
######################################################################################################################
