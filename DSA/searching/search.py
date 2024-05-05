# Normal search,
# Given a list and a number input >> we have to find the index of the given number in the list...

"""
Time Complexity: O(n)
Space Complexity: O(1)
This normal solution takes more time for search the element in list, So we are going for 'Binary Search'
"""

lis = list(map(int, input("Enter ele separated by ',':").split(',')))
num = int(input("Enter a number"))
for i in range(len(lis)):
    if lis[i] == num:
        print(i)

