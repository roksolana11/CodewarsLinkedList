def stringify(node):
    """Convert a linked list to a string"""
    result = ""
    while node:
        result += f"{node.data}" + " -> "
        node = node.next

    result += "None"
    return result
