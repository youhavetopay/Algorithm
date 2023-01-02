# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        list1_data = []
        list2_data = []

        pointer = list1

        while pointer:
            list1_data.append(pointer.val)
            pointer = pointer.next
        
        pointer = list2
        while pointer:
            list2_data.append(pointer.val)
            pointer = pointer.next

        idx1 = 0
        idx2 = 0

        list1_length = len(list1_data)
        list2_length = len(list2_data)

        head = None
        pointer = head

        while idx1 < list1_length or idx2 < list2_length:
            new_node = None

            if idx1 < list1_length and idx2 < list2_length:

                if list1_data[idx1] < list2_data[idx2]:
                    new_node = ListNode(list1_data[idx1])
                    idx1 += 1
                else:
                    new_node = ListNode(list2_data[idx2])
                    idx2 += 1

            elif idx1 < list1_length:
                new_node = ListNode(list1_data[idx1])
                idx1 += 1
            elif idx2 < list2_length:
                new_node = ListNode(list2_data[idx2])
                idx2 += 1

            if head == None:
                head = new_node
                pointer = head
            else:
                pointer.next = new_node
                pointer = new_node

        return head