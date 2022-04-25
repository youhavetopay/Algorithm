# 1. Two Sum
# 두 수의 합
# 난이도 : ★


# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

from typing import List
def twoSum(nums: List[int], target: int) -> List[int]: # 내가 한 풀이

    nums_length = len(nums)

    for i in range(nums_length):
        for j in range(i+1, nums_length):
            if nums[i] + nums[j] == target: # O(n^2)
                return [i, j]



def twoSum(nums: List[int], target: int) -> List[int]: # 첫번째 풀이 최적화

    number_dict = {}
    for i, value in enumerate(nums):
        number_dict[value] = i

    
    for i, value in enumerate(nums):
        try:
            if i != number_dict[target-value]:
                return [i, number_dict[target-value]]  # 현재 인덱스의 값을 뺀 값이 존재한다면 return 
        except KeyError:
            pass

print(twoSum([2,7,11,15], 9))