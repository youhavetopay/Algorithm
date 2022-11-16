class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def compare_lists(llist1, llist2):

    p1 = llist1
    p2 = llist2

    while p1 != None and p2 != None:
        if p1.data != p2.data:
            return 0
        
        p1 = p1.next
        p2 = p2.next
    
    if p1 == None and p2 == None:
        return 1

    return 0


