from typing import List

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        '''
            나의 풀이
            배열에서 k 번째로 큰 수 반환하는 문제
            (O(n) 으로 풀어야 한다고 함)

            그냥 heap 써서 풀었음
            파이썬에서는 최소 힙 밖에 지원을 안해서
            - 를 붙여줘서 넣고
            빼고 나서는 다시 -1 를 곱해주는 방식으로 품

            heap을 직접 구현을 해보는게 좋았을려나...???
        '''

        heap = []

        for num in nums:
            heapq.heappush(heap, -num)

        answer = 0
        for _ in range(k):
            answer = heapq.heappop()

        return answer * -1
    
    def firstSoul(self, nums: List[int], k: int) -> int:

        '''
            첫번째 책 풀이

            나랑 똑같이 heap을 이용했고 -를 붙여줘서 하는 방법으로 품
        '''

        heap = list()

        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)
    
    def secondSoul(self, nums: List[int], k: int) -> int:
        
        '''
            두번째 책 풀이

            heapify라는 메서드를 사용하여 nums를 힙을 만족하도록 변경
            대신 추가하면 깨짐
            하지만 문제에서는 더 이상 힙에 추가하는일이 없으니
            heapify 한번이면 충분함

            이게 이전의 풀이랑 비교해서 시간은 차이가 거의 없는데
            공간복잡도가 엄청 줄어듬
            -> 아마 nums를 새로 만드는게 아니라서 그런듯??
        '''

        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
    
    def thirdSoul(self, nums: List[int], k: int) -> int:

        '''
            세번째 책 풀이
            heapq에는 n번째 숫자가 큰 걸로 순서대로 리스트를 만들어주는 기능이 있음
        '''

        return heapq.nlargest(k, nums)[-1]
    
    def fourthSoul(self, nums: List[int], k: int) -> int:
        
        '''
            네번째 책 풀이
            거꾸로 정렬해서 품
            이게 가장 빠른 방법이라고 함.. ㅋㅋㅋㅋ
        '''

        return sorted(nums, reverse=True)[k-1]