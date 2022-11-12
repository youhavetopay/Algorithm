class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNode(llist, position):
    
    pointer = llist

    count = 0

    if position == 0:
        return pointer.next

    while count < position-1 and pointer.next != None:
        pointer = pointer.next
        count += 1
    
    

    delete_node = pointer.next

    next_node = delete_node.next

    pointer.next = next_node

    return llist