class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

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

