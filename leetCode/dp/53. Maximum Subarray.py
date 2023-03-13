from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        '''
            나의 풀이(못품 ㅠㅠ)

            리스트에서 연속된 부분 리스트의 최대합을 구하는 문제

            DP 문제라고 하는데
            점화식도 모르겠고 어떻게 DP로 풀어야할지도 모르겠움,,
            상황이 상황인지라ㅋㅋㅋ 집중도 안됨 ㅋㅋ
        '''

        max_value = nums[0]
        start = 0
        for i in range(1, len(nums)):
            
            now_i = start + 1
            while max_value < nums[i]:
                now_i += 1
                max_value = sum(nums[start:now_i])

            print(max_value, start)

        return max_value
    
    def firstSoul(self, nums: List[int]) -> int:

        '''
            첫번째 책 풀이
            메모제이션을 활용한 풀이

            이전값이 0보다 크면 더하고 아니면 넘어가는 방식
            그렇게 되면 누적합??와 같이 최대합이 만들어짐
        '''

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)
    
    def secondSoul(self, nums: List[int]) -> int:
        
        '''
            두번째 책 풀이
            카데인 알고리즘을 활용한 풀이
            부분 리스트의 최대합을 구하는 문제는 유명한 알고리즘 문제라고 함
            그래서 카데인이라는 사람이 O(n)으로 풀 수 있는 방법을 고안했다고 함

            각 단계마다 최대값을 저장해서 품
            위에 풀이랑 거의 유사하다고 볼 수 있다고 함        
        ''' 

        best_sum = float('-inf')
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)

        return best_sum

obj = Solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))