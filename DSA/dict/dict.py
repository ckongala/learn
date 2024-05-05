# Dictionary. (also known as associative arrays)
# Collection of key-value pairs
# Un-ordered
# All 'Keys' must be distinct whereas 'Values' may be repeated.
# Using Hashing Internally  >> Faster

d = {110: "abc", 101: "xyz", 105: "pqr"}
print(d)
d["laptop"] = 100000
d["mobile"] = 2000
d["earphones"] = 200  # Inserting
print(d)
print(d["mobile"])  # accessing, if key not present in the dict, it raises an error, so we use get() to access.
print(d.get(101))  # accessing the corresponding values of the key by using get
print(d.get(1000))  # Gives 'None' by default, doesn't raise error, None is special datatype.
print(d.get(1000, 'NA'))  # instead of none we can use base thing.
d[101] = "why"
print(d)  # update the old thing.
print(len(d))
print(d.pop(110))  # remove key-value pair for the given key. and print the value of the deleted key,
del d[105]  # delete the key-value pair but doesn't print the value.
print(d)
d[108] = "cde"
print(d.popitem())  # it removes the last inserted key-value pair. and gives the key-value in tuple


"""

"""