# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pointer = head
        next_node = None
        new_head = None
        pre_node = None

        if pointer:
            next_node = pointer.next
        
        while pointer and next_node:
            if new_head == None:
                new_head = next_node
            
            print(pointer.val, next_node.val, 'pre')
            next_next_node = next_node.next

            next_node.next = pointer
            pointer.next = next_next_node

            if pre_node:
                pre_node.next = next_node
                
            pre_node = pointer

            pointer = pointer.next

            if pointer:
                next_node = pointer.next

            # print(pointer.val, next_node.val)

        if new_head:
            return new_head

        return head
    
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4

so = Solution()

head = so.swapPairs(n1)
test = head
while test:
    print(test.val)
    test = test.next
