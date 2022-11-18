class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDuplicates(llist):
    # Write your code here

    pointer = llist
    data = {}
    while pointer != None:
        data[pointer.data] = 1
        pointer = pointer.next

    head = None
    last_node = head
    for key, value in data.items():
        if head == None:
            head = SinglyLinkedListNode(key)
            last_node = head
        else:
            new_node = SinglyLinkedListNode(key)
            last_node.next = new_node
            last_node = new_node

    return head