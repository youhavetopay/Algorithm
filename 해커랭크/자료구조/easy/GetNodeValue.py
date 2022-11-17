class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def getNode(llist, positionFromTail):
    # Write your code here

    data_list = []
    pointer = llist

    while pointer != None:
        data_list.append(pointer.data)
        pointer = pointer.next

    


    return
