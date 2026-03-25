def swap_pairs(head):
    if not head or not head.next:
        return head

    new_head = head.next
    prev = None
    curr = head

    while curr and curr.next:
        nxt = curr.next
        after = nxt.next
        nxt.next = curr
        curr.next = after
        if prev:
            prev.next = nxt

        prev = curr
        curr = after

    return new_head
