# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        data_list = []

        pointer = head

        while pointer:
            data_list.append(pointer.val)

            pointer = pointer.next

        left = 0
        right = len(data_list) - 1

        while left < right:
            if data_list[left] != data_list[right]:
                return False
            left += 1
            right -= 1

        return True