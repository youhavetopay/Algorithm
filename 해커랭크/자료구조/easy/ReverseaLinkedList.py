class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(llist):
    # Write your code here

    pointer = llist
    data_list = []

    while pointer != None:
        data_list.append(pointer.data)
        pointer = pointer.next

    new_head = None
    last_node = None
    for idx, data in enumerate(reversed(data_list)):
        if idx == 0:
            new_head = SinglyLinkedListNode(data)
            last_node = new_head
        else:
            new_node = SinglyLinkedListNode(data)
            last_node.next = new_node
            last_node = new_node

    return new_head


