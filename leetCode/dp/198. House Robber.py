from typing import List
import collections

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        '''
            나의 풀이
            리스트에서 연속되지 않게 뽑은 숫자들의 합의 최대값을 구하는 문제

            3번째 부터 시작해서 이전에서 자신이 선택할 수 있는 최대값들 중 최대값을 더해서 찾는 방법으로 품
            솔직히 이렇게 해서 풀릴거라고 생각을 못함
            정답이더라도 시간초과에 걸려서 틀릴 줄 알았는데
            이제보니 데이터 크기가 100밖에 안되서
            완전탐색으로만 안하면 풀리는듯?

            좀 어이없게 품 ㅋㅋㅋ
        '''

        for i in range(2, len(nums)):
            nums[i] = max(nums[:i-1]) + nums[i]

        return max(nums)
    
    def firstSoul(self, nums: List[int]) -> int:

        '''
            첫번째 책 풀이(시간초과)
            재귀로 모든 경우의 수를 계산하는 문제
            1단계 전값이랑 2단계전값 + 현재값 중 최대값을 찾아서 푸는 방법
            
            -> 연속되게 선택할 수 없으니까

        '''

        def _rob(i: int) -> int:
            if i < 0:
                return 0
            
            return max(_rob(i-1), _rob(i-2) + nums[i]) 
        
        return _rob(len(nums)-1)
    
    def secondSoul(self, nums: List[int]) -> int:

        '''
            두번째 풀이 방법
            타뷸레이션을 이용한 풀이
            첫번째 풀이에서 이전에 계산한 값은 계산하지 않도록
            메모제이션을 사용함
            옛날 파이썬에서는 딕셔너리 자료형은 추가된 순서를 허용하지 않지만
            OrderedDict을 사용해서 리스트처럼 순서를 기억하도록 할 수 있음

            첫번째 풀이랑 굉장히 유사함

            근데 내 풀이가 시간복잡도 좀더 높음 ㅎㅎㅎㅎㅎ
            대신 공간복잡도는 내가 더 않좋음 ㅋㅋ
        '''

        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        dp = collections.OrderedDict()

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp.popitem()[1]