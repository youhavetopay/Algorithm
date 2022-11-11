class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeAtPosition(llist, data, position):
    # Write your code here

    pointer = llist
    idx = 0
    while idx < position-1:
        pointer = pointer.next
        idx += 1
    
    new_node = SinglyLinkedListNode(data)
    if pointer.next:
        next_node = pointer.next
        pointer.next = new_node
        new_node.next = next_node
    else:
        pointer.next = new_node

    return llist