from typing import List, Set
import bisect

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        '''
            첫번째 나의 풀이
            두 개의 배열의 교집합을 구하는 문제 (순서는 상관없음)

            파이썬에는 집합 자료형이 있기 때문에
            너무 쉽게 풀림
        '''

        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        return list(set_nums1.intersection(set_nums2))
    
    def secondIntersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        '''
            두번째 나의 풀이
            intersection 메소드 사용 안한 풀이
            그래봤자 집합 자료형을 사용했긴 했지만..그래도..??

            이진탐색을 했는데
            이진탐색을 하기위해 nums2를 정렬함
            그 후 nums1에서 각각의 원소들을 nums2에서 찾아서 
            있으면 담는 방법으로 품

            아무래도 첫번째 풀이보다는 시간복잡도가 낮게 나옴
            위에껀 89%, 이거는 37%
        '''

        intersection_nums = set([])

        nums2.sort()
        
        for num in nums1:

            if num in intersection_nums:
                continue
            
            start, end = 0, len(nums2) - 1
            while start <= end:
                mid = start + (end - start) // 2

                if nums2[mid] < num:
                    start = mid + 1
                elif nums2[mid] > num:
                    end = mid - 1
                else:
                    intersection_nums.add(num)
                    break
            
        return list(intersection_nums)
    
    def firstSoul(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        '''
            첫번째 책 풀이
            그냥 완전탐색으로 품 ㅋㅋㅋ
            이게 풀리네..????

            이제 봤는데 최대 데이터 개수가 각각 1000이라서 아슬아슬하게 풀리는듯??
            시간복잡도 6% ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        '''
        
        result: Set = set()

        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)

        return result

    def secondSoul(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        '''
            두번째 나의 풀이
            두번째 나의 풀이랑 똑같음
            대신 bisect 모듈을 사용해서 품
            bisect 라이브러리 꼭 기억하자!!
        '''

        result: Set = set()
        nums2.sort()
        
        for n1 in nums1:
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)
        
        return result

    def thirdSoul(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        '''
            세번째 풀이
            투포인터??를 활용한 풀이
            둘다 정렬한다음에
            처음부터 비교를 시작해서 푸는 방법

            시간복잡도는 조금 낮은데 공간복잡도는 좀 좋은듯???
            참 다양한 풀이가 있는듯 함
        '''

        result: Set = set()

        nums1.sort()
        nums2.sort()

        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        
        return result