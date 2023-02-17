from typing import List
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''
            나의 풀이
            정렬된 배열에서 target 숫자의 index를 반환하는 문제


            이진 탐색으로 구현함
            문제 자체가 이진탐색으로 푸는 문제라서
            그냥 단순하게 구현함
            이진탐색이 뭔지만 안다면 쉽게 푸는 듯??
        '''

        left, right = 0, len(nums)-1
        

        if target < nums[left] or nums[right] < target:
            return -1
        
        while left <= right:
            center = (left + right) // 2
            print(left, right, center)

            if nums[center] == target:
                return center
            
            if nums[center] < target:
                left = center + 1
            else:
                right = center - 1


        return -1
    
    def firstSoul(self, nums: List[int], target: int) -> int:

        '''
            첫번째 책 풀이
            재귀를 통해 이진탐색을 구현함

            재귀로 구현한건 처음 봐서 신기했음 ㅋㅋ
        '''

        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums)-1)
    
    def secondSoul(self, nums: List[int], target: int) -> int:
        
        '''
            두번째 책 풀이
            반복문을 통한 이진탐색 구현함

            나랑 코드가 거의 유사함
            차이점이라면 내 코드의 약간의 최적화가 있다는 것??
            큰 차이는 없을 듯..
        '''


        left, right = 0, len(nums)-1
        while left <= right:

            # 파이썬에서는 임의 정밀도 정수형을 지원해서 이렇게 해도 상관없음
            # 근데 자료형이 엄격한 곳에서는 오버플로우가 발생할 수 있음
            # 그래서 mid = left + (right - left) // 2 이렇게 해야 오버플로우가 안뜸
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1
    
    def thirdSoul(self, nums: List[int], target: int) -> int:
        
        '''
            세번째 책 풀이
            파이썬에 bisect 라는 모듈을 통해 이진 탐색을 구현함
            bisect_left를 하면 왼쪽에서 해당 인덱스를 반환함
        '''

        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
    
    def fourthSoul(self, nums: List[int], target: int) -> int:

        '''
            네번째 책 풀이
            index 메소드를 통해 구현

            나도 처음에 이거 생각했는데 log n으로 풀라고 해서
            안될줄 암 ㅋㅋ -> index는 O(n) 일텐데??
            아슬아슬하게 통과함 ㅋㅋㅋㅋ 시간복잡도 28% ㅋㅌㅋㅋ

            책 내용을 보니 찾으려는 내용이 뒤에 있을 수록 탐색에 걸리는 시간이 늘어남
            -> 즉 index의 최악의 시간복잡도가 O(n)임
            근데 이진탐색은 무조건 log n이라서 데이터 크기가 클 수록 이진탐색이 좋다고 함
        '''

        try:
            return nums.index(target)
        except ValueError:
            return -1

obj = Solution()
print(obj.search([-1,0,3,5,9,12], 2))