# Sorting in Python.
# Two methods sort() and sorted()
# sort()  >> Only works for List and Sorts in-place (changes in original list) >> Time Complexity:- [O(n log(n))]
# sorted() >> works for any iterable(list, tuple, string, dictionary, set) and doesn't modify the passed container,
# returns a new list of sorted items >> Time Complexity:- [O(n log(n))]
# Both are stable & use 'Tim-Sort algorithm'( Hybrid algorithm internally use merge-sort & insertion-sort) > O(n log(n))
######################################################################################################################

# Stability:- If you have two keys, with same value, their original order is retained.
# Ex:- if we have two same values in container, then their order is according to the original
# l = [(1, 10), (2, 20), (3, 30), (1,5), (1,2)]
# Here sorting takes places by taking 1st item, but we have 3 items as same
# so the order is retained by original
# O/P:- [(1, 10), (1, 5), (1,2), (2,20), (3,30)]  order retained when two values are same >>
# so we can say that sorting algorith that used above is stable
# Stability is useful for objects with many fields(more than one) and sorting according to set of fields
# Bubble sort, Insertion sort, Merge sort:- Stable
# Selection sort, Quick sort, Heap sort:- Unstable

#####################################################################################################################
# Sort() Method in python >> Time Complexity:- [O(n log(n))]
# Stable >> uses Timsort >> only works for list(mutable) >> modifies the same list.
# we can't use sort() to tuple and string because they are immutable.
l1 = [5, 10, 15, 1]
l1.sort()
print(l1)  # Sorted the original list.

l2 = [1, 5, 3, 10]
l2.sort(reverse=True)
print(l2)  # sorted the original list in reverse order.

l3 = ["abc", 'ide', 'python', 'dsa']
l3.sort()
print(l3)  # sorted by alphabetical order.


# New Thing !!!!! sorted by the function return type
# In the below ex we are going to sort the list by 'len()'

def my_fun(s):
    return len(s)


l = ['python', 'dsa', 'abc', 'ide']
l.sort(key=my_fun)  # sorting with key parameter >> we can provide function, this function evaluated for every item
# in the list, they are compare according to the return value of the function.
print(l)

l.sort(key=my_fun, reverse=True)  # Optional parameters.
print(l)
#######################################################################################################################

# Sorted() >> Time Complexity:- [O(n log(n))]
# works for any iterable(list, tuple, set, dict, string) > always returns sorted items list >> parameters allow
lsi = [12, -13, -2, 10, 11]
ls = sorted(lsi, key=abs, reverse=True)  # abs = absolute value of integer, just taking value without sign
print(lsi)  # original list doesn't modify,
print(ls)  # always return type <list> in new variable.

tup = (10, 12, 5, 23, 15)
print(sorted(tup))  # taken tuple and return new <list> with sorted order

se = {"python", "dsa", "course"}
print(sorted(se))  # taken set and return new <list> with sorted order

st = 'python'
print(sorted(st))  # taken string and return new <list> with sorted order

dic = {10: 'ck', 2: "dsa", 20: "course"}
print(sorted(dic))  # taken dict and return new <list> with sorted order

listup = [(1, 20), (16, 15), (3, 15)]
print(sorted(listup))  # sorted according to 1st items in each tuple.
#######################################################################################################################
