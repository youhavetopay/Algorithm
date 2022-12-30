from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = []

        length = len(nums)

        total_num = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                continue

            total_num *= num

        if zero_count > 1:
            return [0] * length

        for num in nums:
            if num == 0:
                answer.append(total_num)
            else:
                if zero_count >= 1:
                    answer.append(0)
                else:
                    answer.append(int(total_num/num)) # 나누기 하지 말랬음...ㅋㅋ


        return answer

    def secondSoul(self, nums: List[int]) -> List[int]:

        '''
            나를 기준(나 제외)으로 처음부터 왼쪽까지
            나를 기준(나 제외)으로 오른쪽부터 끝까지 곱한 것을 곱해주면 됨..ㅋ
            
        '''

        answer = []
        
        init_val = 1
        for num in nums: # 왼쪽까지의 곱한 값 구하기
            answer.append(init_val)
            init_val *= num
            
        
        init_val = 1
        for i in range(len(nums)-1, -1, -1): # 오른쪽부터 곱한 값 구하기
            answer[i] *= init_val # 왼쪽 값 구한거에 곱해주기
            init_val *= nums[i]


        return answer