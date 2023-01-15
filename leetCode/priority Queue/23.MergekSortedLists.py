# Definition for singly-linked list.
from typing import List, Optional

from heapq import heappop, heappush

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        '''
            나의 풀이
            여러개의 연결리스트를 병합해서 정렬하는 문제

            그냥 반복문으로 연결리스트의 데이터 전부 담고
            데이터를 다시 반복문으로 새로 연결리스트를 만들어서 반환함
            그랬던니 통과..?

            책에서 우선순위 큐라고 되어있어서 일단 한번 풀었는데 
            통과해서 당황함..

            심지어 이 문제 hard ㅋㅋ
        '''

        datas = []

        for data_list in lists:
            pointer = data_list

            while pointer:
                datas.append(pointer.val)
                pointer = pointer.next

        datas.sort()

        head = None
        pointer = None

        for data in datas:
            if head == None:
                head = ListNode(data)
                pointer = head
            else:
                new_node = ListNode(data)
                pointer.next = new_node
                pointer = pointer.next

        return head
    

    def firstSoul(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        '''
            책 풀이

            우선순위 큐를 바탕으로 품
            근데 우선순위 큐는 파이썬에서는 heapq를 사용해서 한다고 함
            별도의 priorityQueue 라는 모듈이 있는데 여기 내부 구현에서도 
            heapq를 사용하고 있음

            이 둘의 차이는 스레드 세이프 관련 차이라고 하는데
            크게 신경안써도 되서 그냥 heapq를 사용하는 것을 권장하고 있다고 함


            암튼 heap에 처음에 연결리스트의 head를 담고
            그 다음에 하나씩 꺼내면서 새로운 연결리스트르 만들고
            연결리스트의 다음 값을 다시 heap에 추가함
            -> 최소 힙이기 때문에 낮은 순서대로 나오기에 자동으로 정렬됨

            그리고 단순히 ListNode.val을 담으면 중복이 생겨서 별도의 인덱스를 heap에 같이 넣어서 
            중복을 방지함
            -> 파이썬 heapq에서는 중복된 값은 넣을 수 없나봄..
        '''

        root = result = ListNode(None)

        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heappush(heap, (result.next.val, idx, result.next))

        return root.next