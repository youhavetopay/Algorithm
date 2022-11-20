class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def reverse(llist):
    # Write your code here

    pointer = llist

    data_list = []
    while pointer != None:
        data_list.append(pointer.data)
        pointer = pointer.next

    data_list.reverse()

    head_node = None
    last_node = None
    for idx, data in enumerate(data_list):
        if idx == 0:
            head_node = DoublyLinkedListNode(data)
            last_node = head_node
        else:
            new_node = DoublyLinkedListNode(data)
            last_node.next = new_node
            new_node.prev = last_node
            last_node = new_node
    
    return head_node