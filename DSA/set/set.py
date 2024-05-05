# SET
# It support collection of same items or different items as well
# Distinct Elements >> Unordered >> No indexing
# Faster in Operations like 'search', 'delete', 'insert' because it is using "HASHING"
# Union, Intersection, Set Difference,.... are faster
# using Hashing Internally.

s1 = {10, 20, 30}
print(s1)  # Order is not same while printing multiple times.
s2 = set([20, 30, 40])  # Set constructor., we can use 'list', 'tuple' as input to get 'set' as output
print(s2)
s3 = {}  # It of type dict
print(type(s3))
s4 = set()
print(type(s4))  # type 'set'

print(len(s1))  # print length of the set
print(20 in s1)  # Membership operation support in set
print(50 in s1)

s5 = {10, 20}
s5.add(30)  # added the element to the set.
print(s5, "s5")
s5.add(30)  # Set only allows distinct items.
print(s5, "2nd s5")
s5.update([40, 50], {60, 70}, (80, 90))  # using 'update' we can add from other collections,(list, set, tuple)
print(s5, "3rd s5")

s5.discard(30)  # If item present in the set > remove item, if item not present in the list it will do nothing.
print(s5, "4th s5")
s5.remove(50)  # If item present in the set > remove item, if item not present in the list it will raise an error.
print(s5, "5th s5")
s5.clear()  # remove all the elements in the set. makes >> empty set().
print(s5, "6th s5")
del s5  # delete the set, no more s5, removes the object.
# if we use s5 below the del s5, we get an error.

s6 = {2, 4, 6, 8}
s7 = {3, 6, 9}

print(s6 | s7, "union using operator.")  # printing union of the two sets using 'union' operator
print(s6.union(s7), "union using method.")  # union of the two set using method, It doesn't change the original sets.
print(s6)

print(s6 & s7, "intersection using operations ")  # printing intersection of the two numbers.
print(s6.intersection(s7), "using method")
print(s7)

print(s6 - s7, "difference")  # prints ele present in s1 not in s2
print(s6.difference(s7), "difference")  # prints difference

print(s6 ^ s7)  # symmetric difference operator.
print(s6.symmetric_difference(s7))

s8 = {2, 4, 6, 8}
s9 = {4, 8}

print(s8.isdisjoint(s9))  # return true when there is no common ele in the sets
print(s8 <= s9)  # >> s8.issubset(s9)
print(s8 < s9)  # proper subset or not.
print(s8 >= s9)  # >> s8.issuperset(s9) superset or not
print(s8 > s9)  # proper superset or not.

