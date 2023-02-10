# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
            첫번째 나의 풀이
            연결리스트의 값을 기준으로 정렬하는 문제

            간단하게 배열에 모든 값을 담고 sort 으로 정렬시키고
            다시 연결리스트 만드는 아주 간단하고 무식한?? 방법으로 품 ㅋㅋㅋ

            근데 문제에서 공간복잡도도 한번 줄여보라고 해서 
            연결리스트 자체에서 정렬시키는 방법을 찾아보는게 좋을 듯 함
        '''

        datas = []

        pointer = head

        while pointer:
            datas.append(pointer.val)
            pointer = pointer.next

        datas.sort()

        new_head = None
        pre_node = new_head
        for data in datas:
            
            new_node = ListNode(data)

            if new_head is None:
                new_head = new_node
                pre_node = new_head
                continue
                
            pre_node.next = new_node
            pre_node = pre_node.next

        return new_head

    def secondSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
            두번째 나의 풀이

            어찌저찌 병합정렬로 풀어봤는데
            이게 맞나........?

            연결리스트를 새로 안만들고 자기 위치에서 이동시켰는데
            너무 복잡해짐
            
            첫번째 풀이에 비해
            공간복잡도는 확실히 줄었지만 45mb -> 36.4mb
            시간복잡도는 겁나 늘어남 400ms -> 900ms
        '''

        if head is None:
            return None

        def merge(left, right):

            new_head = None
            tail = None
            left_head = left
            right_head = right

            while left_head or right_head:
                
                if left_head and right_head:
                    
                    if left_head.val <= right_head.val:
                        if new_head is None:
                            new_head = left_head
                            tail = new_head
                        else:
                            tail.next = left_head
                            tail = tail.next

                        left_head = left_head.next
                        

                    else:
                        if new_head is None:
                            new_head = right_head
                            tail = new_head
                        else:
                            tail.next = right_head
                            tail = tail.next

                        right_head = right_head.next
                        

                elif left_head:
                    
                    if new_head is None:
                        new_head = left_head
                        tail = new_head
                    else:
                        tail.next = left_head
                        tail = tail.next
                    left_head = left_head.next
                    

                else:
                    if new_head is None:
                        new_head = right_head
                        tail = new_head
                    else:
                        tail.next = right_head
                        tail = tail.next

                    right_head = right_head.next
                    
        
            return new_head

        def divsion(node):

            total_length = 0
            p = node
            while p:
                p = p.next
                total_length += 1
            
            if total_length == 1:
                return node

            pre = node
            right = node
            right_idx = 0
            while right_idx < total_length // 2:
                pre = right
                right = right.next
                right_idx += 1
            
            pre.next = None

            left = node

            if total_length > 2:
                left = divsion(node)
                right = divsion(right)

        
            new_head = merge(left, right)
            

            return new_head
                

        return divsion(head)


    def mergeTwoLists(self, l1:ListNode, l2: ListNode) -> ListNode:

        # 정렬하는 메서드
        # 이걸 어떻게 생각해.... ㅠㅠ
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            
            l1.next = self.mergeTwoLists(l1.next, l2)
        
        return l1 or l2

    def firstSoul(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
            첫번째 책 풀이
            병합정렬로 아주 깔끔하게 품 ㄷㄷ

            런너 기법을 통해 연결리스트의 절반지점?? 을 구함

            시간복잡도는 나의 두번째 풀이보다 조금 좋음 50ms 정도?
            근데 공간복잡도는 85.8mb ..

            그나마 내가 잘한건가...? ㅋㅋㅋㅋㅋㅋ
        '''

        if not (head and head.next):
            return head

        # 연결리스트는 길이를 알 수가 없어서 
        # 이렇게 구함
        # slow 는 한칸씩 fast는 두칸씩 가고
        # fast 가 끝까지 가면 한칸씩 가던 slow가 중간지점임
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next

        half.next = None

        # 재귀로 분할
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        # 정렬된 리스트 반환
        return self.mergeTwoLists(l1, l2)
    
    def secondSoul(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
            두번째 풀이
            나의 첫번째 풀이랑 비슷한데
            연결리스트를 새로 만드는 것이 아니라
            기존에 있는 애들의 값만 바꿔줌 ㄷㄷ

            이게 가장 좋음
            시간 260ms, 공간 36.5mb ㄷㄷ
        '''

        p = head
        lst = []

        while p:
            lst.append(p.val)
            p = p.next
        
        lst.sort()
        # 여기까지는 똑같음

        # 여기서 lst에 담은 걸 반복문으로 돌면서
        # 값을 담아줌
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next

        return head

t1 = ListNode(4)
t2 = ListNode(2)
t3 = ListNode(1)
t4 = ListNode(3)
t5 = ListNode(9)

t1.next = t2
t2.next = t3


obj = Solution()
print(obj.secondSortList(t1))