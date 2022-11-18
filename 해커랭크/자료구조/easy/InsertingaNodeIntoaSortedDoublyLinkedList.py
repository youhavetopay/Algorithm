class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def sortedInsert(llist, data):
    # Write your code here

    head = llist
    pointer = llist
    while pointer != None:
        if pointer.data < data:
            if pointer.next == None:
                new_node = DoublyLinkedListNode(data)
                pointer.next = new_node
                new_node.prev = pointer
                return head

            pointer = pointer.next

        else:
            if pointer == head:
                new_node = DoublyLinkedListNode(data)
                new_node.next = head
                head.prev = new_node
                return new_node

            prev_node = pointer.prev
            new_node = DoublyLinkedListNode(data)
            prev_node.next = new_node

            new_node.prev = prev_node
            new_node.next = pointer

            pointer.prev = new_node
            return head



    