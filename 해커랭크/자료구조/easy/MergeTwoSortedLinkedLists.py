class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeLists(head1, head2):

    p1 = head1
    p2 = head2

    data_list = []
    while p1 != None:
        data_list.append(p1.data)
        p1 = p1.next

    while p2 != None:
        data_list.append(p2.data)
        p2 = p2.next
    
    data_list.sort()

    new_head = None
    last_node = new_head
    for data in data_list:
        if last_node == None:
            new_head = SinglyLinkedListNode(data)
            last_node = new_head
        else:
            new_node = SinglyLinkedListNode(data)
            last_node.next = new_node
            last_node = new_node

    return new_head