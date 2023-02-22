from typing import List

import collections

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        '''
            나의 풀이
            배열에서 하나만 있는 요소 찾는 문제

            그냥 defaultdict에 개수를 저장해서
            1 인 걸 찾아서 반환하는 방식으로 품

        '''

        nums_counts = collections.defaultdict(int)

        for num in nums:
            nums_counts[num] += 1

        for key, value in nums_counts.items():
            if value == 1:
                return key

        return
    
    def firstSoul(self, nums: List[int]) -> int:

        '''
            책 풀이
            XOR 연산을 이용해서 품
            
            XOR 연산은 입력값이 서로 다르면 True
            같으면 False가 되는데
            이러한 특징을 이용해서
            두번 등장한 숫자는 0으로 초기화 되고 
            한번만 등장하는 숫자는 그 값을 온전히 보전함

            배열에 모든 값에 XOR 연산을 하면 단 한번만 등장하는 숫자만 남게됨
            ㄷㄷ
        '''

        result = 0
        for num in nums:
            result ^= num
        
        return result