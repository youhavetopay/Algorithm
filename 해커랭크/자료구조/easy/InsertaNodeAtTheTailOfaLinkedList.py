def insertNodeAtTail(head, data):

    pointer = head

    if not pointer:
        pointer = SinglyLinkedListNode(data)
        return pointer

    while pointer.next != None:
        pointer = pointer.next
    
    new_node = SinglyLinkedListNode(data)
    pointer.next = new_node

    return head

