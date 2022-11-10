class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeAtHead(llist, data):
    
    head_node = llist
    new_node = SinglyLinkedListNode(data)
    
    print(printLinkedList(llist))
    print()
    
    if head_node == None:
        return new_node
    
    new_node.next = head_node
    
    
    return new_node

def printLinkedList(head):

    pointer = head

    while pointer != None:
        print(pointer.data)
        pointer = pointer.next

    return

llist = SinglyLinkedListNode(0)

for _ in range(5):
    llist_item = int(input())
    llist_head = insertNodeAtHead(llist, llist_item)
    llist = llist_head

print()
print(printLinkedList(llist))