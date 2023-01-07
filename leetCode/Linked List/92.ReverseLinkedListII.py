# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
            나의 풀이
            그냥 left 번째 노드부터 right번째 노드까지 리스트에
            담아서 다시 연결시켜주는 방법
        '''

        if left == 1 and left == right:
            return head

        idx = 1
        node_list = []

        pointer = head

        tail_node = None

        while idx <= right:

            if idx + 1 == left:
                tail_node = pointer

            if idx >= left:
                node_list.append(pointer)
            
            idx += 1
            pointer = pointer.next


        last_node = node_list[-1].next
        node_list.reverse()
        
        pre_node = None
        for i, node in enumerate(node_list):
            if i == 0:
                if tail_node != None:
                    tail_node.next = node
                
            else:
                pre_node.next = node
            
            pre_node = node

        if last_node:
            pre_node.next = last_node
        else:
            pre_node.next = None

        if tail_node == None:
            return node_list[0]

        return head

    def firstSoul(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        '''
            책 풀이

            start, end를 기준으로 이동하면서 계속 변경시킴
            start : left-1 번째 노드
            end : left 번째 노드

        '''

        # 예외처리
        if not head or left == right:
            return head

        root = ListNode(None)
        root.next = head
        start = root

        for _ in range(left-1):
            start = start.next
        
        end = start.next

        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        
        return root.next