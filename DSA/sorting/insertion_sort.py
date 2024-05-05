# Insertion sort
"""
Simple Sorting algorithm.
>> In-place and Stable.
>> Used for small sized arrays(Tim sort and Intra sort).
>> Time Complexity:-
In Worst Case(given list in reversed order:- O(n^2))
and In Best Case(given list in sorted order:- O(n))
>> Space Complexity:- O(1) so it is In-place algorithm

>> Explanation :-
"""

l = [12, 10, 2, 15, 4, 5]
n = len(l)
for i in range(1, n):
    x = l[i]
    j = i - 1
    while j >= 0 and x < l[j]:
        l[j + 1] = l[j]
        j = j - 1
    l[j + 1] = x

print(l)
