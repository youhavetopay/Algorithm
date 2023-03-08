# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
            나의 풀이
            
            정렬된 연결리스트의 중복노드를 제거하는 문제

            쉬웠음
            연결리스트를 순회하면서 값이 다르면 이어주는 방식으로 품
            easy라서 그런지 엄청 쉬웠음 ㅋㅋ
        '''

        if head is None:
            return None
        
        now_tail = head
        pointer = now_tail.next
        
        while pointer:
            
            if now_tail.val != pointer.val:
                now_tail.next = pointer
                now_tail = pointer

            pointer = pointer.next

        now_tail.next = None

        return head