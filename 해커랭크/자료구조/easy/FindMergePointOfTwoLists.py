class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMergeNode(head1, head2):

    node_list = []

    pointer = head1
    while pointer != None:
        node_list.append(pointer)
        pointer = pointer.next

    pointer = head2
    while pointer != None:
        for node in node_list:
            if node == pointer:
                return pointer.data
        
        pointer = pointer.next

    return 0

