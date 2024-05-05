# Only useful for Sorted list

"""
Point to be remembered, Binary search is used for Sorted List.
Time Complexity :- O(log n),
Space Complexity is O(1).
The binary search is efficient for large lists as it quickly narrows down the search space by half in each iteration.
"""


# Given Sorted list and a number input >> we have to find the index of the given number in the list.

def binary_search(lis, k):
    low = 0
    high = len(lis) - 1
    while low <= high:
        mid = (low + high) // 2
        if lis[mid] == k:
            return mid
        elif lis[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1


lis = [1, 2, 3, 4, 5, 6, 7, 8]  # Given Sorted List.
k = 10
print(binary_search(lis, k))

#######################################################################################################################

# Binary Search Using recursion
"""
Time Complexity :- O(log n),
Space Complexity:- O(log n).
"""


def binary_recursive_search(l, k, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if l[mid] == k:
        return mid
    elif l[mid] > k:
        return binary_recursive_search(l, k, low, mid - 1)
    else:
        return binary_recursive_search(l, k, mid + 1, high)


lis0 = [1, 2, 3, 4, 5, 6]
k0 = 5
low0 = 0
high0 = len(lis0) - 1
print(binary_recursive_search(lis0, k0, low0, high0))

#######################################################################################################################

# Given Sorted List and number input, We have to found the 1st occurrence of the number in the list.
"""
Normal Solution 
Time Complexity: O(n)
Space Complexity: O(1)
"""


def first_occur(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
        return -1


arr1 = [1, 2, 3, 4, 4, 5, 6]
n1 = len(arr1)
x1 = 4
print(first_occur(arr1, n1, x1))

"""
using binary we reduce time.
Time Complexity: O(log(n))
Space Complexity: O(log(n))
While using of recursion, Space Complexity is O(log(n)) >> So it is better to use Iterative (while, for)
"""


def first_occur_recursion(arr, low, high, x):
    if low > high:
        return -1
    mid = (low + high) // 2
    if x > arr[mid]:
        return first_occur_recursion(arr, mid + 1, high, x)
    elif x < arr[mid]:
        return first_occur_recursion(arr, low, mid - 1, x)
    else:
        if mid == 0 or arr[mid - 1] != arr[mid]:
            return mid
        else:
            return first_occur_recursion(arr, low, mid - 1, x)


arr2 = [1, 2, 3, 4, 5, 6]
low2 = 0
high2 = len(arr2) - 1
x2 = 3
print(first_occur_recursion(arr2, low2, high2, x2))

"""
using binary we reduce time.
Time Complexity: O(log(n))
Space Complexity: O(1)
While using of Iteration, Space Complexity is O(1) > So it is better to use Iterative(while,for) compare with Recursion
"""


def first_occur_iter(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if x > arr[mid]:
            low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != arr[mid]:
                return mid
            else:
                high = mid - 1
    return -1


arr3 = [1, 2, 3, 5, 5, 5, 5, 6, 7, 8]
x3 = 5
print(first_occur_iter(arr3, x3))

#######################################################################################################################

# Given Sorted List and number input, We have to found the last occurrence of the number in the list.
"""
Normal Solution 
Time Complexity: O(n)
Space Complexity: O(1)
"""


def last_occur(list1, num1):
    for i in reversed(range(len(list1))):
        if list1[i] == num1:
            return i
    return -1


list1 = [1, 2, 3, 4, 4, 4, 4, 5, 6]
num1 = 4
print(last_occur(list1, num1))

"""
Using Binary Search  
Time Complexity: O(log(n))
Space Complexity: O(1)
"""


def last_iter_effective(list2, num2):
    low = 0
    high = len(list2) - 1
    while low <= high:
        mid = (low + high) // 2
        if list2[mid] < num2:
            low = mid + 1
        elif list2[mid] > num2:
            high = mid - 1
        else:
            if mid == high or list2[mid] != list2[mid + 1]:
                return mid
            else:
                low = mid + 1


list2 = [1, 2, 3, 4, 4, 4, 4, 5, 6]
num2 = 4
print(last_iter_effective(list2, num2))

#######################################################################################################################
# Count Occurrence in a sorted array
# Given Sorted List and number, return the count of number in the list
"""
Using methods
Time Complexity of the code is O(n),
Space Complexity is O(1).
"""


def count(li, x):
    return li.count(x)


def count1(li1, y):
    count = 0
    for i in range(len(li1)):
        if li1[i] == y:
            count += 1
    return count


li = [1, 2, 3, 4, 5, 6, 6, 7]
x = 6
print(count1(li, x))
print(count(li, x))

"""
Simple Binary Search 
Using First Occurrence and Last Occurrence we acn find the count.
Time Complexity of the below code is O(log(n)),
Space Complexity is O(1). 
"""


def countOccurr(l, x):
    first = first_occur_iter(l, x)

    if first == -1:
        return 0

    else:
        return last_iter_effective(l, x) - first + 1


l = [10, 20, 20, 20, 30, 30]

print(10, countOccurr(l, 10))


######################################################################################################################
# Count of 1's in a sorted binary list.
# Given sorted list, we have to find the number of 1's in the given list.

# Formula:- len (list) - first_occur() + 1

def binary_count(list_bin):
    occur = first_occur_iter(list_bin, 1)
    return len(list_bin) - 1 - occur + 1


list_bin = [0, 0, 0, 0, 1, 1, 1, 1, 1]
print("----", binary_count(list_bin))
