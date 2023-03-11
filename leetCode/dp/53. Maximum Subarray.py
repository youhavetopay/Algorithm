from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_value = float("-inf")

        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                max_value = max(max_value, sum(nums[i:j]))

        return max_value