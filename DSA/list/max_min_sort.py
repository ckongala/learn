# Given a list of number we have to find the MAX item in the list.

# METHOD -1  # print(max(lis))
# METHOD -2
"""
Time Complexity: :-O(N), where N is the number of elements in the list
Space Complexity: :- O(1)
"""
k = list(map(int, input("Enter list items separate by ','").split(',')))
z = 0
for i in k:
    if i > z:
        z = i
print(z)
#####################################################################################################################
# Given a list, we have to found the MIN item in the list.
# METHOD -1  # print(min(lis))
# METHOD -2
"""
Time Complexity: :-O(N), where N is the number of elements in the list
Space Complexity: :- O(1)
"""
k1 = list(map(int, input("Enter list items separate by ','").split(',')))
z1 = k1[0]
for i in k1:
    if i < z1:
        z1 = i
print(z1)
######################################################################################################################
# Given a list, we have to found the second-largest item in the list.
"""
Time Complexity: :-O(N), where N is the number of elements in the list
Space Complexity: :- O(1)
"""
k3 = list(map(int, input("Enter list items separate by ','").split(',')))
max1 = 0
max2 = 0
for i in k3:
    if i > max1:
        max1 = i
for j in k3:
    if max2 < j < max1:
        max2 = j
print(max2)
######################################################################################################################
# Given a list, we have to found the second-Minimum item in the list.
"""
Time Complexity: :-O(N), where N is the number of elements in the list
Space Complexity: :- O(1)
"""
k4 = list(map(int, input("Enter list items separated by ','").split(',')))
min1 = float('inf')  # Initialize min1 to positive infinity
min2 = float('inf')  # Initialize min2 to positive infinity

for i in k4:
    if i < min1:
        min2 = min1
        min1 = i
    elif i < min2 and i != min1:
        min2 = i

print(min2)


#####################################################################################################################
# Check if a list is in Sorted.

# METHOD -1
def is_sorted_list(l1):
    # i = 1
    # while i < len(l1):
    for i in range(1, len(l1)):
        if l1[i] < l1[i - 1]:
            return False
        # i+=1
    return True


# METHOD -2

def is_sorted(l):
    sl = sorted(l)
    if sl == l:
        return True
    else:
        return False


lis = list(map(int, input("Enter ele separate by ',': ").split(',')))
print(is_sorted_list(lis))
print(is_sorted(lis))
#######################################################################################################################
# Reverse a list we are following different approach's..


lis1 = list(map(int, input("Enter ele separate by ',': ").split(',')))
lis1.reverse()
print(lis1)  # Reverse the same list

new_l = list(reversed(lis1))  # Returns a new reversed list
print(new_l)

new_l1 = lis1[::-1]  # Return a new reversed list
print(new_l1)

"""
Time Complexity: :-O(N/2), where N is the number of elements in the list
Space Complexity: :- O(1)
"""
z = len(lis1)
for k in range(0, len(lis1) // 2):
    lis1[k], lis1[z - k - 1] = lis1[z - k - 1], lis1[k]  # Swapping technique to reverse the ele in list
print(lis1)
# using while loop
# """
# Time Complexity: :-O(N), where N is the number of elements in the list
# Space Complexity: :- O(1)
# """
# s = 0
# e = len(lis1) - 1
# while s < e:
#     lis1[s], lis1[e] = lis1[e], lis1[s]
#     s += 1
#     e -= 1
# print(lis1)

#####################################################################################################################
# removing Duplicates in list
"""
Time Complexity:- O(N^2),
Space Complexity:- O(N), where N is the number of elements in the list
"""
lis3 = list(map(int, input("Enter ele separate by ',': ").split(',')))
or_list = []
for i in lis3:
    if i not in or_list:
        or_list.append(i)
print(or_list)

#####################################################################################################################
# left rotate a list by one
lis4 = list(map(int, input("Enter ele separate by ',': ").split(',')))
lis4 = lis4[1:] + lis4[0:1]  # OR
lis4.append(lis4.pop(0))  # OR


def rotatebyone(lis4):
    n = len(lis4)
    x = lis4[0]
    for i in range(1, n):
        lis4[i - 1] = lis4[i]
    lis4[n - 1] = x
    return lis4


print(rotatebyone(lis4))
