"""Parsing a linked list from a string"""
class Node:
    """class Node"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    """Parsing a linked list from a string"""
    list_words = list_repr.split(" -> ")[:-1]
    head = None
    for value in reversed(list_words):
        head = Node(int(value), head)
    return head
