# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
            나의 풀이
            연결리스트 삽입 정렬하는 문제
            
            148. Sort List 처럼 풀어도 상관은 없겠지만
            그래도 삽입정렬을 하라고 했으니 어찌 저찌 구현함..ㅋㅋㅋ
            좀 어려웠음 ㅋㅋ
        '''

        if head is None:
            return None

        pre_head = ListNode()
        pre_head.next = head
        p = head

        # 끝가지 반복
        while p:
            p_next = p.next
            pre = pre_head
            now = pre_head.next

            # 정렬된 리스트부터 비교
            # 현재 노드보다 크면 반복 종료
            while now.val <= p.val:
                pre = now
                now = now.next

                # 끝까지 왔으면
                # 해당 노드가 마지막 노드
                if now is None:
                    if pre.val != p.val:
                        p.next = None
                    break
            else:
                pre.next = p
                p.next = now

            p = p_next

        return pre_head.next
    
    def firstSoul(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
            첫번째 책 풀이
            삽입정렬로 품

            나보다 코드도 훨~~씬 간단하고 공간복잡도도 좋음
            대신 시간복잡도는 쪼~~끔 좋지 않음

            이렇게 간단하다고?? ㅋㅋㅋ 나 뭐한거야 ㅋㅋㅋ
        '''

        cur = parent = ListNode(None)

        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next

            cur = parent

        return cur.next
    
    def secondSoul(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
            두번째 책 풀이
            첫번째 풀이를 개선한 버전
            엄청 줄어듬 ㅋㅋ 거의 1500ms 줄어듬 ㅋㅋ

            원래 삽입정렬은 정렬된 리스트를 비교를 시작할 때
            가장 큰값에서 왼쪽으로 시작을 하는데
            연결리스트라서 제일 처음부터 비교를 시작해야함 -> 그래서 좀 비효율적??

            그래서 무조건 처음부터 가는 것이 아니라
            비교한 값의 이전값이 head보다 크다면 처음으로 이동하는 방식으로 개선함
        '''

        cur = parent = ListNode(0)

        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next

            if head and cur.val > head.val:
                cur = parent

        return parent.next

l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(0)

l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5

obj = Solution()
print(obj.insertionSortList(l1))