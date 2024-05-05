# String.
print("ascii value of 'a' is", ord("a"))  # Gives ASCII value for the given single character
print("character of given value is", chr(97))  # Gives the character for the given ASCII Value.
str1 = "I am maabbu"
print(f'Hey, {str1} \n \\n I\'m feeling incomplete!!!')  # \ operator is for escape the character.
print(r"Hi,  I'm felling the same >> C:\name.py")  # Raw string, whatever you write in string as it is comes as output
print(f'upper case of {str1} is {str1.upper()}')
print("print index", str1.index('b'))  # Gives the First Occurrence Index.
print("prints right index", str1.rindex('b'))  # Gives the Last Occurrence Index.
print("prints range of index", str1.index('b', 3, 10))  # Start search from given range.
print("a" in str1)  # Member operator, checks substring and return bool.
print("ab" in str1)
print("au" in str1)
print("maa" not in str1)
print("abc" > "ab")  # Checks the ASCII Value by character from start to end
print("abc" > "ABC")
print(len(str1))  # Gives length of the string
print(str1.lower())  # Return lower case of the list
print(str1.upper())  # Return upper case of the list
print(str1.isupper())  # Checks all are upper or not and  return bool
print(str1.startswith("m", 0, len(str1)))  # return Bool >> checks for the start index...
print(str1.endswith("u"))  # return Bool
print(str1.split())  # >> gives list
l = ['abc', 'xyz']
print(",".join(l))  # takes list and gives result as string
s = "@@@abcdef@@@"
print(s.strip("@"))  # Strip is used to remove unwanted characters in str
print(s.lstrip("@"))  # removes left
print(s.rstrip('@'))  # removes Right
print(s.find('@@@'))  # gives the stating index
print(s.find("aaaa"))  # return -1, because string doesn't have
print(s.find("@@@", 2, len(s)))  # search in range
#  Difference between index and find, if an item is not in the list 'index' gives error whereas 'find' gives -1
#######################################################################################################################
#  Reverse the string
"""
Time Complexity:- O(n),
Space Complexity:- O(1).
"""
rev = ''
for i in s:
    rev = i + rev
print(rev)
#  Using slice
print(s[::-1])  # Same as above O(n) and O(1)
#######################################################################################################################
#  For the given string we have to print all the possible sub-strings.
"""
Time Complexity:- O(n^2),
Space Complexity:- O(n^2),
"""


def all_substrings(s):
    n = len(s)
    substrings = []

    for start in range(n):
        for end in range(start + 1, n + 1):
            substrings.append(s[start:end])

    return substrings


# Test the function
input_string = "abcd"
result = all_substrings(input_string)
print(result)

#######################################################################################################################
#  Check for Rotation either left or right rotation by either number of times.
#  Takes as input, check for the rotation
#  Input:- ABCD, Check:- BCDA >> CDAB >> DABC >> DABC >> CDAB

"""
Time Complexity:- O(log(n)),
Space Complexity:- O(1). 
"""


def are_rotations(s1, s2):
    if len(s1) != len(s2):
        return False
    temp = ''
    temp = s1 + s1
    return temp.find(s2) != -1


s1 = "abcd"
s2 = "bcda"
print(are_rotations(s1, s2))
#######################################################################################################################
# Checking of the palindrome

"""
Time Complexity :- O(n),
Space Complexity:- O(1).
"""
st = 'abcd'

low = 0
high = len(st) - 1

while low <= high:
    if st[low] != st[high]:
        print("Not a palindrome")
        break
    low = low + 1
    high = high - 1
else:
    print("Palindrome")
#  One thing has to remember is while loop has 'else' part !!!!!!!IMP!!!!!!
# Another method
if st == st[::-1]:
    print("palindrome")
else:
    print("not a palindrome")  # Same as above O(n), O(1).

#######################################################################################################################
#  Check if a string is subsequence of other
# Given input "abc", subsequence are >> a, b, c, ab, ac, bc, abc #here 'ba' is not a subsequence.
# sub-strings are continuous character whereas sub-sequences are missing some character in original.
# 'ac' can be sub-sequence but not a sub-string.
# Total number of subsequence is:- formula(2 pow(n))

#  For the given string we have to print all the possible sub-strings
"""
Time Complexity:-  O(2^n),
Space Complexity:-  O(2^n)
"""


def all_subsequences(s):
    n = len(s)
    subsequences = []

    # The number of possible subsequences is 2^n
    num_subsequences = 1 << n
    for i in range(num_subsequences):
        subsequence = ""
        for j in range(n):
            if i & (1 << j):
                subsequence += s[j]
        subsequences.append(subsequence)

    return subsequences


# Test the function
input_string = "abc"
result = all_subsequences(input_string)
print(result)

"""
Time Complexity:- O(n),
Space Complexity:- O(1)
"""


def is_sub_seq(s1, s2):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == len(s2):
        return True
    else:
        return False


# Using recursion  # not best approach.
"""
Time Complexity:- O(n)
Space Complexity:- O(n)
"""


def is_sub_seq_recursion(s1, s2, m, n):
    if n == 0:
        return True
    if m == 0:
        return False
    if s1[n - 1] == s2[m - 1]:
        return is_sub_seq_recursion(s1, s2, m - 1, n - 1)
    else:
        return is_sub_seq_recursion(s1, s2, m - 1, n)


#######################################################################################################################
# Anagram
# Given two string we have to find these can form anagram or not
# Definition:- Checking whether sequencer can form permutations of each other (order may vary)
# (every character in string1 is in string2 or not) >> if Yes, return 'True' else "False".
# Example:- s1 = 'listen' and s2 = 'silent'  >> s1 and s2 from an Anagram.

def are_anagram(s1, s2):
    if len(s1) == len(s2):
        s1 = sorted(s1)
        s2 = sorted(s2)
        return s1 == s2
    return False


# Best approach ########################
# Idea:- Use count array. because string data type have fixed and small length of number ASCII (256) and continuous.
"""
Time Complexity: O(n) in the worst case, where n is the length of the longest input string. 
Space Complexity: O(n + m) in the worst case, where n is the length of the first input string (s1) and m is the length
 of the second input string (s2).
"""


def are_anagram_strings(s1, s2):
    if len(s1) != len(s2):
        return False
    count = [0] * 256  # List of 256 zeroes [0, 0, 0,...]
    for i in range(len(s1)):
        count[ord(s1[i])] += 1  # ord >> Return ASCII value.
        count[ord(s2[i])] -= 1
    for x in count:
        if x != 0:
            return False
    return True


######################################################################################################################
# reverse the words
# Given String 'welcome to dsa' >> output as 'dsa to welcome'
"""
Time complexity: O(n) - where n is the length of the input string.
Space complexity: O(n) - where n is the length of the input string.
"""
string99 = "welcome to dsa"

lis99 = string99.split(' ')

k99 = ''
n99 = len(lis99) - 1

for i in range(n99, -1, -1):
    k99 = k99 + " " + lis99[i]

print(k99)  # dsa to welcome
######################################################################################################################
# Leftmost Repeating Character.
# Examples:- str = "abbcc" > o/p:- 1 > return index of 'b' because 'b'  is the left most repeating character.
"""
Time complexity: O(n ^ 2) - where n is the length of the input string.
Space complexity: O(n) 
"""
sem1 = 'abcdff'


def abcd(s1):
    for i in range(len(s1)):
        for j in range(i + 1, len(s1)):
            if s1[i] == s1[j]:
                return i
    return -1


print(abcd(sem1))

# Best approach
# Idea:- use count array

"""
Time complexity: O(n) - where n is the length of the input string.
Space complexity: O(n) 
"""


def leftmost(str1):
    count = [0] * 256
    for i in range(len(str1)):
        count[ord(str1[i])] += 1
    for i in range(len(str)):
        if count[ord(str[i])] > 1:
            return i
    return -1


print(leftmost(sem1))

####################################################################################################################
# left most non-repeating element
# Ex:- str1 = "abcabc" >> all are repeating character spo return -1
# Ex:- str1 = "apple" >> o/p:- 0 >> Because 'a' is left most not repeating character
"""
Time complexity: O(n) in the worst case, where n is the length of the input string s1.
Space complexity: O(n) in the worst case, where n is the length of the input string s1.
"""


def left_most_non(s1):
    count = [0] * 256
    for i in range(len(s1)):
        count[ord(s1[i])] += 2
    for x in range(len(s1)):
        if count[ord(s1[x])] == 2:
            return x
    return -1


sem2 = 'abvabd'
print(left_most_non(sem2))


