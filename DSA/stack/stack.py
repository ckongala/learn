"""
STACK:- Just think of bucket,
It follows 'First in Last out(FILO)'
In python implementation of stack data structure is by using "list" or "dequeue"
In case of stack :-
List and Deque both provide constant time for push and pop operation.

Operations:-

isempty :- Returns bool true if the stack is empty, else false >> in python use if condition (if li: or  if not li:)

push(x) :- Insert an item to the top of the stack.  >> in python push == append

pop() :- Remove an item from the top.

peek() :- Return the top item.  >> in python we use index "-1"

size() :- Return the size of the stack.  >> in python we use len().

Corner condition on stack operations:-

Underflow: when pop() or peek() called on empty stack

Overflow: when push called on full stack.
"""
"""
Application:- wherever FILO then use stack...
1. Function calls...
2. Balanced Parenthesis [(a+b)*[c+(d-e)]]
3. Reversing Items
4. Infix to Pastfix/prefix and Evaluation of Postfix/Prefix
(( 
>> Infix a+b 
>> prefix +ab 
>> postfix ab+ 
))
5. Stock span problem and its varients
6. undo/redo or Forward/Backward in google
"""

"""
Stack in Python:-
1. using list
2. using collections.deque (mainly based on doubley-linked list)
3. using queue.LIFOqueue ( advanced topic, used in multi-thread environment)
4. using our own implementation.
"""

#  1. Using list
# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack.pop())
# peek = stack[-1]
# print(peek)
# size = len(stack)
# print(size)

# 2. using collections.deque
# deque is mainly based on doubly-linked list

# from collections import deque
# stack = deque()
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack.pop())
# peek = stack[-1]
# print(peek)
# size = len(stack)
# print(size)

# List is cache friendly and it's worst case time complexity is linear but majorly it's O(1).
# In case of dequeue, it uses doubly-linked list, worst case time complexity is O(1) but it's not cache friendly.
# list is likely to be use more


# 3. Linked list implementation of stack in Python...
import math


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class MyStack:
    def __init__(self):
        self.head = None
        self.sz = 0

    def push(self, x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.sz = self.sz + 1

    def size(self):
        return self.sz

    def peek(self):
        if self.head == None:
            return math.inf
        return self.head.data

    def pop(self):
        if self.head == None:
            return math.inf
        res = self.head.data
        self.head = self.head.next
        self.sz = self.sz - 1
        return res


s = MyStack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.peek())
print(s.size())
# Time complexity is O(1)


