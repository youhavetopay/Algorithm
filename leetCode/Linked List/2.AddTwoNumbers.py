# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        list1_words = []
        list2_words = []

        pointer = l1
        while pointer:
            list1_words.append(pointer.val)
            pointer = pointer.next
        
        pointer = l2
        while pointer:
            list2_words.append(pointer.val)
            pointer = pointer.next
        
        list1_num = ''
        for num in reversed(list1_words):
            list1_num += str(num)
        
        list2_num = ''
        for num in reversed(list2_words):
            list2_num += str(num)
        
        result_num = int(list1_num) + int(list2_num)

        head = None
        pre_node = None
        for num in reversed(str(result_num)):
            if head == None:
                head = ListNode(int(num))
                pre_node = head
            else:
                new_node = ListNode(int(num))
                pre_node.next = new_node
                pre_node = new_node
        


        return head