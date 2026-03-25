class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError
    first_head = None
    first = None
    second_head = None
    second = None

    current = head
    i = 0
    while current:
        next_node = current.next
        current.next = None

        if i % 2 == 0:
            if first_head is None:
                first_head = current
                first = current
            else:
                first.next = current
                first = current
        else:
            if second_head is None:
                second_head = current
                second = current
            else:
                second.next = current
                second = current

        i += 1
        current = next_node

    return Context(first_head, second_head)
