class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def printlist(head):
    """
    Time Complexity:- O(n)
    Aux Space:- O(1)
    :param head:
    :return:
    """
    curr = head
    while curr is not None:
        print(curr.key, end=",")
        curr = curr.next


def search_ele(head, ele):
    """
    Time Complexity:- O(n)
    Space Complexity:- O(1)
    :param head:
    :param ele:
    :return:
    """
    curr = head
    i = 1
    while curr is not None:
        if curr.key == ele:
            return f"Element is found at {i} position"
        curr = curr.next
        i += 1
    else:
        return f"Element is Not Found"


def insert_beg(head, key):
    """
    Time Complexity:- O(1)
    Aux
    :param head:
    :param key:
    :return:
    """
    temp = Node(key)
    temp.next = head
    return temp


def insert_end(head, key):
    """
    Time Complexity :- O(n)
    Aux Space:- O(1)
    If you maintain the last node reff, we can make Time Complexity in O(1).
    :param head:
    :param key:
    :return:
    """
    if head is None:
        return Node(key)
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = Node(key)
    return head


def insert_ele_at_position(head, data, pos):
    temp = Node(data)
    if pos == 1:
        temp.next = head
        return temp
    curr = head
    for i in range(pos - 2):
        curr = curr.next
        if curr is None:
            return head
    temp.next = curr.next  # order is important, if 1st we do curr.next = temp then we will lose remaning linked list
    curr.next = temp
    return head


def delete_beg(head):
    """
    Time Complexity :- O(1)
    Aux Space:- O(1)
    """
    if head is None:
        return None
    else:
        return head.next


def delete_end(head):
    if head is None:
        return None
    if head.next is None:
        return None
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None
    return head

# Just for Printing
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(15)
# head.next.next.next = Node(30)
# printlist(head)


# print(search_ele(head, 30))


# head = None
# head = insert_beg(head, 10)
# head = insert_beg(head, 20)
# head = insert_beg(head, 30)
# printlist(head)


# head = None
# head = insert_end(head, 10)
# head = insert_end(head, 20)
# head = insert_end(head, 30)
# printlist(head)


# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# head.next.next.next.next = Node(50)
# printlist(head)
# head = insert_ele_at_position(head, 45, 25)
# printlist(head)


# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# printlist(head)
# head = delete_beg(head)
# printlist(head)


# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# printlist(head)
# head = delete_end(head)
# printlist(head)


