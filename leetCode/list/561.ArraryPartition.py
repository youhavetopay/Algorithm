from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        nums.sort()

        answer = 0

        temp_list = []
        for num in nums:

            temp_list.append(num)

            if len(temp_list) == 2:
                answer += min(temp_list)
                temp_list = []

        return answer

solu = Solution()


print(solu.arrayPairSum(nums=[1,4,3,2]))