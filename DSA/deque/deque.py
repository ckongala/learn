"""
Deque stands for doubly-ended queue it internally using Doubly linked list.
we can insertions and deletions from both ends.
deque is one of the alternative to implement stack and queue.
other alternative is List. using list we can implement stack and Queue

In case of stack :-
List and Deque both provide constant time for push and pop operation.

In case of Queue:-
List doesn't provide constant time operation for N-queue and D-queue operations but deque allow to in constant time.

Operations:-
1. Insert Front.
2. Delete Front.
3. Insert Rear.
4. Delete Rear.

Additional Operations:-
getFront()
getRear()
isFull()
isEmpty()
size()


Applications:-
1. It can be used as both stack and Queue.
2. Maintain history of action
3. A steal Process scheduling Algo
4. Implementing a priority queue with two types of priority.(if you get 1st priority add at the head otherwise add at the rear)
5. Maximum/Minimum of all sub-arrays of size k in an array
"""

from collections import deque

d = deque()
d.append(10)  # Append on right side(used to append single items)
d.append(20)  # Append on right side.
d.append(30)  # Append on right side.
d.appendleft(5)  # Append on left side.

print(f"printing the entire deque{d}")
print(f"printing the type of {type(d)}")

print(d.pop())  # It removes the right object
print(d.popleft())  # It removes the right object

print(f"after poping the deruee{d}")

# Other operations

d1 = deque([10, 20, 30, 40])  # [10, 20, 30, 40]
d1.insert(2, 10)  # Insert at element "10" at the 2nd position. [10, 20, 10, 30, 40]
print(d1.count(10))  # It will give the count of ele "10" in the deque.
d1.remove(10)  # It removes the first occurrence of the element (simply from the left) [20, 10, 30, 40]
print(d1)
d1.extend([50, 60])  # [20, 10, 30, 40, 50, 60] used to append multiple items on right side.
d1.extendleft([15, 25])  # [25, 15, 20, 10, 30, 40, 50, 60] used to append multiple items on left side.
# Appending in reverse order just have a look on it, i5 append first and 25 append next in left side.
print(d1)

# Other Operations...
d2 = deque([10, 20, 30, 40, 50])
d2.rotate(2)  # [40, 50, 10, 20, 30]  # Rotate in clockwise
print(d2, "rotated d2 is printed")
d2.rotate(-2)  # [10, 20, 30, 40, 50] #
print(d2, "anticlockwise wise rotated d2 is printed here")
d2.reverse()  # [50, 40, 30, 20, 10]
print(d2, "reverse d2 is printed here")

# Index based access.
print(d2[2], "d2[2]")
d2[2] = 100
print(d2, "updated index of d2 is printing here")
print(d2[0], "d2[0] is here")
print(d2[-1], "d2 last item using index.")

# Note:- **** Slicing is not allowed in Deck *****

# deque internally using Doubly linked list functionality.

# NOTE:- Time Complexity and Internal Working.
"""
append(x)---------  O(1)
appendleft(x)-----  O(1)
pop()-------------  O(1)
popleft()---------  O(1)

d[i]------------- O(n)
count(x)--------- O(n)
insert(i, x)----- O(n)

rotate(r) ----------Theta(abs(r))

extend(l) --------- Theta(len(l))
extendleft(l) ----- Theta(len(l))
"""

# 1. Linked List Implementation Of Deque ###########################
"""If we use double linked list, we can do below operations in constant time operation.
Operations:-
insertfront()
insertrear()
deletefront()
deleterear()
getfront()
getrear()
size()
isempty() 
see in double-linked-list-of deque.py"""

# 2. List Implementation of Deque ####################################
"""If we use list, we can do below operations in constant time operation.
Operations:-
insertfront()
insertrear()
getfront()
getrear()
size()
isempty() 

The below two operations are in general liner time operations.
deletefront()
deleterear()
to make them as constant time, We use circular implementation
see in list-imp-of-deque.py file in same folder."""

