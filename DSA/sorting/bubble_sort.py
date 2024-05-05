# Bubble Sort
"""
Simple Compression based algorithm.
>> Stable and In-place algorithm.
>> Time Complexity:- O(n^2)
>> Space Complexity:- O(1) so it is In-place algorithm

>> Explanation :- We have multiple passes, In the first pass we move the largest element to final position
\and in the next pass we move 2nd largest element to the 2nd last position,... until all the elements are moved to the
correct position.

>> working:- we compare the adjacent element beginning from the first element and check the condition, if condition true
we swap both the elements until we get the largest element comes to the last position by the end of the 1st pass.

we do the same process 'n-1' times to sort the 'n' elements.
"""


def bubble_sort(l):
    n = len(l)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    # return l


lis = [10, 8, 20, 5]
bubble_sort(lis)
print(lis)


# If already a sorted list, why we need more iterations??
# Optimized solution
# only one pass for i = 0
# Time Complexity is:- O(n) when we give sorted list.
def bubble_sorted(l):
    for i in range(len(l) - 1):
        swapped = False
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True
        if not swapped:
            return


lis1 = [10, 8, 20, 5]
bubble_sorted(lis1)
print(lis1)
