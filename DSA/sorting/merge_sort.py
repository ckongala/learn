# Merge Sort
# Merging two sorted arrays.

"""
>> Divide and conquer Algorithm
>> Stable Algorithm and not In-place Algorithm
>> Time Complexity:- O(n log(n))
>> Space Complexity:- O(n)
>> well suited for the linked lists. works in O(1) Aux space.
>> Used in external sorting.
"""
"""
Naive Solution
>> Time Complexity:- (M+N)*log(M+N)
>> Space Complexity:- O(m + n),
"""


# Merge Two Sorted Arrays.


def merge_sort(a, b):
    res = a + b
    res.sort()
    return res


# merge two sorted array.
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# print(merge_sort(a, b))

"""
>> Time Complexity:- O(max(m, n))
>> Space Complexity :- O(m + n)
"""
# Merge Two Sorted Arrays.
# a = [10, 15]
# b = [5, 6, 6, 30, 40]
# a = [1,2,3,4,4,5,6,6]
# b = [2,3,4,6,4,5,6,7,8]  # Here b is not sorted, hence we get unsorted list as output
# res = []
# m = len(a)
# n = len(b)
# i = 0
# j = 0
# while i < m and j < n:
#     if a[i] < b[j]:
#         res.append(a[i])
#         i += 1
#     else:
#         res.append(b[j])
#         j += 1
# while i < m:
#     res.append(a[i])
#     i += 1
# while j < n:
#     res.append(b[j])
#     j += 1
#
# print(res)
#######################################################################################################################
# UNION

a = [1, 2, 3, 4, 4, 5, 6, 6]
b = [2, 3, 4, 4, 5, 6, 7, 8]
i = 0
j = 0
m = len(a)
n = len(b)
res = []
# l = a + b
# l.sort()
# k = set(l)
# print(list(k))
while i < len(a) and j < len(b):
    if i > 0 and a[i] == a[i - 1]:
        i += 1
    elif j > 0 and b[j] == b[j - 1]:
        j += 1
    elif a[i] < b[j]:
        res.append(a[i])
        i += 1
    elif a[i] > b[j]:
        res.append(b[j])
        j += 1
    else:
        res.append(a[i])
        i += 1
        j += 1
while i < m:
    if i > 0 and a[i] != a[i - 1]:
        res.append(a[i])
    i += 1
while j < n:
    if j > 0 and b[j] != b[j - 1]:
        res.append(b[j])
    j += 1

print(res)
#######################################################################################################################
# Intersection


a = [3, 5, 8, 10, 10, 15]
b = [2, 8, 9, 10, 15]

m = len(a)
n = len(b)

i = 0
j = 0

res = []
"""
Time Complexity:- 
Space Complexity:-
"""
# for i in range(m):
#     for j in range(n):
#         if a[i] == b[j] and a[i] not in res:
#             res.append(a[i])

"""
Best Approach
Time Complexity
Space Complexity
"""
while i < m and j < n:
    if i > 0 and a[i] == a[i - 1]:
        i += 1
        continue
    if a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        res.append(a[i])
        i += 1
        j += 1

print(res)
