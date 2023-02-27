from typing import List

import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        '''
            나의 풀이 (못품 시간초과..)
            리스트에서 일정 범위의 숫자중 가장 큰 값들을 반환하는 문제

            슬라이딩 윈도우 문제인데
            자꾸 시간초과 뜸

        '''

        # k 가 1이면 그대로 던져주면 됨
        if k == 1:
            return nums

        # k 가 리스트 길이랑 같다면 바로 max해서 던져주기
        if k == len(nums):
            return [max(nums)]

        answer = []

        # 초기값 설정
        # 처음엔 그냥 처음부터 k개 짤라서 max값이랑 index를 구함
        now_nums = nums[:k]
        max_value = max(now_nums)
        max_value_idx = now_nums.index(max_value)
        answer.append(max_value)

        for i in range(k, len(nums)):

            # 새로운 숫자가 max_value보다 크면 해당 값으로 바꾸기
            if max_value <= nums[i]:
                max_value = nums[i]
                max_value_idx = i

            # 현재 max_value가 범위에서 빠졌을 때 새로 갱신
            elif max_value_idx < i - k + 1:
                now_nums = nums[i-k+1:i+1]
                max_value = max(now_nums)
                max_value_idx = now_nums.index(max_value)
                

            answer.append(max_value)

        return answer

    def firstSoul(self, nums: List[int], k: int) -> List[int]:
        
        '''
            첫번째 책 풀이 (시간초과)

            완전탐색으로 차례대로 탐색해서 구하는 풀이
            당연히 이거 시간초과 뜸 ㅋㅋ
        '''


        if not nums:
            return nums
        
        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i+k]))

        return r
    
    def secondSoul(self, nums: List[int], k: int) -> List[int]:
        
        '''
            두번째 책 풀이 (시간초과)

            queue를 사용해서 최대값을 찾아가는 방식
            이것도 시간초과 ㅋㅋㅋㅋㅋㅋㅋ
            아마 데이터가 새로 추가된듯??

            나도 queue로 해봤었지만 시간초과라서 포기했음 ㅋㅋ
        '''

        results = []
        window = collections.deque()
        current_max = float('-inf')

        for i, v in enumerate(nums):

            window.append(v)
            if i < k - 1:
                continue
                
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v
            
            results.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')
        
        return results

    def thirdSoul(self, nums: List[int], k: int) -> List[int]:
        
        '''
            세번째 풀이 (깃허브)

            두번째 풀이가 데이터 추가로 인해 시간초과가 뜸
            그래서 O(n)으로 풀어야 해서 dequeue를 활용해서 품

            와 잘하네...... ㅋㅋ
        '''


        deq, ans = collections.deque(), []

        for i in range(len(nums)):

            # 윈도우 크기 넘어가면 앞에서 빼기
            if deq and i-deq[0] == k:
                deq.popleft()
            
            # deq에 현재 숫자보다 작은건 뒤에서 빼기
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            
            # 값 담아주기
            deq.append(i)

            # 현재 인덱스가 k 이상 일때 부터 넣기
            if i + 1 >= k:
                # deq[0]에는 최대값 인덱스가 담겨 있음
                ans.append(nums[deq[0]])

        
        return ans


obj = Solution()
print(obj.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))