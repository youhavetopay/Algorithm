from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''
            나의 풀이
            순환하면서 정렬된 리스트에서 target 찾는 문제

            대충 리스트가 [x ~ 최대값, 최소값 ~ x 보다 작은 값] 이렇게 되어 있어서
            최대값의 위치를 구해서
            두가지 구간으로 나누어서 이진탐색을 시작함
            1. 첫번째 요소에서 최대값까지의 범위
            2. 최소값(최대값 다음 인덱스) 부터 마지막 요소 까지의 범위
            이 두가지 구간에 없으면 없는 거임
            그 이후 범위를 찾았으니 이진탐색을 실행
            
            처음에 문제를 이해하는데 있어서 조금 시간이 걸렸지만
            문제 자체는 그렇게 어렵지 않았음..
            범위만 잘 구하면 이진탐색하는건 쉬워서 그런듯..???

            이진 탐색 코드를 잘 이해하고 외우고 있어야 할듯함
        '''

        max_index = nums.index(max(nums))

        start, end = 0, 0
        if nums[0] <= target <= nums[max_index]:
            start, end = 0, max_index
        elif max_index + 1 < len(nums) and nums[max_index+1] <= target <= nums[-1]:
            start, end = max_index + 1, len(nums) - 1
        else:
            return -1
        
        while start <= end:
            
            mid = (start + end) // 2

            print(start, end, mid)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1

    
    def firstSoul(self, nums: List[int], target: int) -> int:

        '''
            책 풀이
            최소값을 먼저 구하고
            그 후 이진탐색을 진행하는데
            mid 에 최소값 인덱스를 더하고 길이로 나누는 방식으로(약간 원형큐 접근하는 방법처럼)
            target을 찾아감

            최소값을 찾는 거는 index(min(nums))로도 할 수 있지만 
            최대한 이진탐색을 구현하는게 문제의 의도??라서 직접 찾았다고 함

        '''

        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1 
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot

        return -1

obj = Solution()
print(obj.search([4,5,6,7,0,1,2], 0))