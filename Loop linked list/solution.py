def loop_size(node):
    current = node
    check = node

    while check is not None and check.next is not None:
        current = current.next
        check = check.next.next

        if current == check:
            length = 1
            current = current.next
            while current != check:
                length += 1
                current = current.next
            return length
    return 0
