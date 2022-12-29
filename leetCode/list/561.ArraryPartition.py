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
    
    def secondSoul(self, nums: List[int]) -> int:

        nums.sort()

        answer = 0

        # 어차피 정렬하면 순서 쌍으로 묶는데
        # 앞에 오는 (짝수 번째 요소)만 더해주면 됨
        for i, num in enumerate(nums):
            if i % 2 == 0:
                answer += num

        return answer
    
    def likePython(self, nums: List[int]) -> int:

        # 파이썬의 slice 사용하면 더 간편함.ㅋㅋ
        # 시간복잡도 도 더 낮게 나옴
        return sum(sorted(nums)[::2])
    

solu = Solution()


print(solu.arrayPairSum(nums=[1,4,3,2]))