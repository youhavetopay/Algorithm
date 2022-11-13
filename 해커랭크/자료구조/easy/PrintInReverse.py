class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def reversePrint(llist):
    
    # Write your code here

    data_list = []

    pointer = llist
    while pointer.next != None:

        data_list.append(pointer.data)
        pointer = pointer.next
        
    data_list.append(pointer.data)
    for i in range(len(data_list)-1, -1, -1):
        print(data_list[i])

    return
   