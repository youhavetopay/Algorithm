# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
            나의 풀이
            공간복잡도 제약이 있는지 모르고 품 ㅋㅋ
            리스트를 사용하면 안됨!!
            근데 통과는 함 -> 시간복잡도도 더 낮은듯????(큰 의미는 없는듯)
        '''

        idx = 1
        pointer = head
        pre_node = None
        node_list = [] 

        while pointer:
            if idx % 2 == 0: # 짝수번째 있는 노드는 담기
                node_list.append(pointer)

                # 해당 짝수번째 노드의 다음 노드가 있다면 새로 연결
                if pointer.next: 
                    pre_node.next = pointer.next

            # 마지막 노드라면 끝내기
            # while 조건으로 하면 짝수개의 노드라면 리스트에 안담아서..ㅋ
            if not pointer.next:
                break
            
            # 이전노드 저장
            pre_node = pointer

            # 포인터 이동
            pointer = pointer.next
            idx += 1
        
        # 리스트의 마지막 노드 설정
        tail_node = pointer
        if idx % 2 == 0: # 마지막 노드가 짝수번이라면 이전노드로
            tail_node = pre_node

        # 리스트에 담아둔 노드를 연결시켜주기
        for idx, node in enumerate(node_list):
            tail_node.next = node
            tail_node = node

        if tail_node: # head가 None으로 오는 경우가 있는 듯?
            tail_node.next = None

        return head
    
    def firstSoul(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
            이건 책 풀이
            공간복잡도랑 시간복잡도를 만족시킴
        '''
        
        if not head: # head 가 None으로 오는 경우 처리
            return head
        
        odd = head
        even = head.next
        even_head = even

        # 짝수번째 노드랑 홀수번째 노드를 따로 따로 연결시켜줌!!
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 마지막 노드랑 연결
        odd.next = even_head

        return head