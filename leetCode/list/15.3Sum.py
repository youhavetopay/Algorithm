# 1. 3um
# 세 수의 합
# 난이도 : ★★


# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

from typing import List

import copy
def threeSum(nums: List[int]) -> List[List[int]]: # 나의 풀이 시간복잡도 ㅋㅋ

    answer = []

    nums_length = len(nums)

    for i in range(nums_length-2):
        stack = []
        stack.append(nums[i])
        for j in range(i+1, nums_length-1):
            stack.append(nums[j])
            for p in range(j + 1, nums_length):
               
                if sum(stack) + nums[p] == 0:
                    stack.append(nums[p])

                    temp_stack = copy.deepcopy(stack)
                    
                    temp_stack.sort()
                    if temp_stack not in answer:
                        answer.append(temp_stack)
                        
                    stack.pop()
            stack.pop()
        stack.pop()

    return answer



n1 = [-1,0,1,2,-1,-4]
n2 = [3,0,-2,-1,1,2]
# print(threeSum(n1))
#print(threeSum(n2))

import itertools
def threeSum(nums: List[int]) -> List[List[int]]: # 나의 풀이 2 시간복잡도 ㅋㅋ

    answer = []

    three_nums = list(map(list, itertools.combinations(nums, 3)))

    for num_list in three_nums:
        if sum(num_list) == 0:
            sort_list = sorted(num_list)
            if sort_list not in answer:
                answer.append(sort_list)

    return answer

print(threeSum(n2))


def threeSum(nums: List[int]) -> List[List[int]]: # 풀이 1 브루트 포스 ? 이거 시간복잡도 걸림
    answer = []

    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: # 중복인 숫자는 제외
            continue
        for j in range(len(nums)-1):
            if j > 0 and nums[j] == nums[j-1]: # 중복인 숫자는 제외
                continue
            for k in range(len(nums)):
                if k > 0 and nums[k] == nums[k-1]: # 중복인 숫자는 제외
                    continue
                if sum(nums[i], nums[j], nums[k]) == 0:
                    answer.append([nums[i], nums[j], nums[k]])

    return answer


def threeSum(nums: List[int]) -> List[List[int]]: # 풀이 2 투포인터 활용
    answer = []

    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: # 중복인 숫자는 제외
            continue
        
        # 첫번째 숫자를 찾았으니 나머지 뒷부분의 숫자를 투포인터로 찾기

        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum < 0: # 숫자가 작을 경우 left를 한칸 앞으로(정렬되어 있으므로)
                left += 1
            elif sum > 0: # 숫자가 높을 경우 right를 한칸 뒤로 (정렬되어 있으므로)
                right -= 1
            elif sum == 0:

                answer.append([nums[i], nums[left], nums[right]]) # 정답을 추가

                while left < right and nums[left] == nums[left + 1]: # 중복된 숫자를 피하기 위해 앞 숫자랑 같을 경우 한칸 앞으로
                    left += 1
                while left < right and nums[right] == nums[right - 1]: # 중복된 숫자를 피하기 위해 뒤 숫자랑 같을 경우 한칸 뒤로
                    right -= 1

                left += 1 # 다음칸으로 이동
                right -= 1 # 다음칸으로 이동


    return answer

print(threeSum(n2))