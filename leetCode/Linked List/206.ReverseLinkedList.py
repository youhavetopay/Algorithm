# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        data_list = []

        pointer = head

        while pointer:
            data_list.append(pointer.val)
            pointer = pointer.next
        
        data_list.reverse()

        new_head = None
        pointer = new_head
        for data in data_list:
            if new_head == None:
                new_head = ListNode(data)
                pointer = new_head
            else:
                new_node = ListNode(data)
                pointer.next = new_node
                pointer = pointer.next

        return new_head