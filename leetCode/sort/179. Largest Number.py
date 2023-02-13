from typing import List
import collections

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        '''
            나의 풀이(못품...)
            숫자들을 문자열로 더해서 가장 큰 수를 찾는 문제

            이것저것 다해봤지만 결국 못품..ㅠㅠ
            그냥 앞자리가 높은 순으로 정렬을 하면 되는데
            이런식으로 51, 5 가 있을 때는 5가 먼저 와야하는 예외가 있음
            근데 이 예외가 어쩔때는 자리수가 낮은게 앞으로 올때도 있고
            뒤로 가야할때도 있는데 정확히 어떤 규칙에 의해 결정되는지를 못찾음
            그래서 못품 ㅠㅠ

            내가 정렬이라는 분야의 문제에 많이 약한듯..
        '''

        num_max_length = 0
        
        str_nums = []
        for idx, num in enumerate(nums):
            str_num = str(num)
            
            str_nums += [str_num, str_num],
            num_max_length = max(num_max_length, len(str_num))

        for idx in range(len(str_nums)):
            
            if len(str_nums[idx][0]) < num_max_length:
                plus_word = '0'
                if str_nums[idx][0][0] <= str_nums[idx][0][-1]:
                    plus_word = str_nums[idx][0][0]

                str_nums[idx][0] += str_nums[idx][0][0]

                while len(str_nums[idx][0]) < num_max_length:
                    str_nums[idx][0] += plus_word

        str_nums.sort(reverse=True, key=lambda x:(x[0], -len(x[1])))
        print(str_nums)


        answer = ''
        for _, num in str_nums:
            answer += num

        return answer



    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def firstSoul(self, nums: List[int]) -> str:

        '''
            책 풀이
            뜨하 또 뻘짓 했네 ㅋㅋㅋㅋㅋ
            삽입정렬을 응용하여 풀면 됨

            인근 두자리를 대소 비교를 하면서
            자리를 바꿔주면 됨...
        '''

        i = 1

        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j - 1], nums[j]

                j -= 1
            
            i += 1
        
        # 입력값이 [0, 0] 이 있어서
        # "00" 으로 나오는 걸 "0"으로 바꿔줘야 함
        return str(int(''.join(map(str, nums))))

obj = Solution()
print(obj.largestNumber([432,43243]))