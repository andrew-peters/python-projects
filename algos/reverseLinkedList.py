def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None # To point to the previous node
    curr = head # To hold the current node
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev