l = [10, 20, 30, 40]

# Advantages:- Random Access and Cache Friendly
# Disadvantages:- Insertion, Deletion, Unordered list search are time taking >> disadvantages are overcome by 'SET'

# In list 'append' and 'pop' are constant time ### Best to use###.
# 'Insertion', 'deletion', 'search (except sorted list > binary search)' are linear time

print(l)
l.append(100)  # added the ele at the end. # It takes constant time to append the ele in list
l.insert(1, 70)  # added the element at the given index.
print(10 in l)  # return bool , 'in' is a member operator.
l.count(10)  # return the count of the element in the list.
l.index(10)  # return the starting index of the element when two or more elements in list.
# l.index(30, 0, 3)  # start index include, end index exclude, return index for the element in range.
l.reverse()  # reverse the given list, we have to print list to see the result
l.sort()  # by default, it sorts the list in asc order (when only all the elements in the list are same type)
l.remove(20)  # remove element by using element
l.pop()  # remove element at the end of the list
l.pop(2)  # remove element by using index.
del l[1]  # deleting element by using index.
del l[0:2]  # deleting elements in the range
# print(max(l))  # return max item in the list when only all the elements in the list are same type
# print(min(l))  # return min item in the list when only all the elements in the list are same type
# print(sum(l))  # return sum of ele in the list, (only works when all the list ele are numbers)
####################################################################################################################
# Average or Mean of the list
# METHOD -1
lis = list(map(int, input("Enter list elements separated by ',' ").split(',')))
print(sum(lis) / len(lis))

# METHOD -2
"""
The Time Complexity:- O(N), # N is the number of elements in the input list l1.
Space Complexity:- O(1)
"""


def average(l1):
    sum1 = 0
    count = 0
    for x in l1:
        sum1 = sum1 + x
        count += 1
    print(count)
    print(sum1)
    return sum1 / count


l1 = [10, 20, 30, 40]
print(average(l1))
################################################################################################################
# Separate Even and Odd elements in list

"""
The Time Complexity:- O(N), # N is the number of elements in the input list l2.
Space Complexity:- O(1)
"""


def separate(l2):
    even = []
    odd = []
    for x in l2:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return even, odd  # we get returned value as tuple... i.e,([even],[odd])


l2 = list(map(int, input("Enter list element separately by space").split(" ")))
even, odd = separate(l2)  # here we are unpacking the tuple getting to lists as separate.
print(even)
print(odd)
####################################################################################################################
# Slicing (Important Concept)
"""
List, Tuple, Strings are supported by slicing,
In case of 'list' we always get the different 'list' when we slice, whereas in 'string' and 'tuple' address to the same 
items because of they are immutable, so tuples are faster as compare to list
Just want to focus on it works
Formula:-
l[start: end: step] >> l[start] + l[start + step] + l[start + 2*step] ...until end, here end is excluded!!!

"""
# Example
li = [10, 20, 30, 40, 50]
print(li[0:5:1])  # OUTPUT:- [10,20,30,40,50]
# print(li[-3: 'any number': 1])  # OUTPUT:- [30. 40, 50]
print(li[-1: -6: -1])  # OUTPUT:- [50, 40, 30, 20, 10]
# working Explanation :- ONLY FOCUS ON STATING INDEX AND ADD THE STEP
# ...MOVES IN ONE-WAY >> index -3, -2, -1 then ends not goes to start
# starts from -1 index,
# >> adding -1(start) to -1(step),
# >> adding -1(start) to 2(factor) * -1(step)
# >> adding -1(start) to 3(factor) * -1(step) ....

######################################################################################################################
"""
In case of 'list' we always get the different 'list' when we slice, whereas in 'string' and 'tuple' address to the same 
items in below example
list1 and list2 are two separate memory locations whereas t1 and t2 address to the same memory location and
s1 and s2 address to the same memory location.
Tuple and string are immutable, so tuples are faster as compare to list.
"""
list1 = [10, 20, 30]
list2 = list1[:]

t1 = (10, 20, 30)
t2 = t1[:]

s1 = "abcd"
s2 = s1[:]

print(list1 is list2)  # False
print(t1 is t2)  # True
print(s1 is s2)  # True
##################################################################################################################
"""
Comprehensions supports List, set, Dictionary
below are dictionary example...
"""
# Reverse keys and values
d1 = {101: 'abc', 102: 'qwe', 103: 'asd'}
d2 = {v: k for (k, v) in d1.items()}
print(d2)  # {'abc': 101, 'qwe':102, 'asd':103}

#######################################################################################################################
# Len of distinct items in the list
"""

"""
ap = [10, 20, 10, 30, 40, 50, 20, 10, 2]

count = 1
for i in range(1, len(ap)):
    if ap[i] not in ap[0:i]:
        count += 1
print(count)
