# Selection sort
"""
Simple Compression based algorithm.
>> Not Stable and In-place algorithm.
>> Time Complexity:- O(n^2)
>> Space Complexity:- O(1) so it is In-place algorithm
>> Does less memory writes compared to quicksort, mergesort, insertionsort,..etc,
But 'cycle sort' is optimal in terms of memory writes.
>> Basic idea for heap sort
>> In-place algorithm, doesn't require extra memory for sorting.


>> Explanation:- we find out the min element and put it on the 1st place similarly we find the 2nd min ele and put it
over the 2nd place process repeats until all ele are sorted.
if we have n elements we need to iterate (n-1) times to sort all ele in list.
"""


def selection_sort(l):
    n = len(l)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if l[j] < l[min_ind]:
                min_ind = j
        l[min_ind], l[i] = l[i], l[min_ind]


lis = [10, 5, 8, 20, 2, 18]
selection_sort(lis)
print(lis)
