from typing import List

class Solution:

    def firstSoul(self, prices: List[int]) -> int:

        # 맨 처음 작성했던 풀이

        max_profit = 0

        for i in range(len(prices)): 
            for j in range(i,len(prices)): # 나보다 뒤에 있는 가격중 가장 큰 차이 찾기
                max_profit = max(max_profit, prices[j]-prices[i])

        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        # 두번째 풀이
        '''
            나의 위치에서 왼쪽에서 최소 값을 찾아서 빼는게 정답
            이렇게 하면 O(n)
        '''

        max_profit = 0

        # 초기 최소값 설정
        min_price = 999999999999999999

        for price in prices:
            min_price = min(min_price, price) # 현재 값 이랑 이전의 최소값 비교
            max_profit = max(price-min_price, max_profit)


        return max_profit

a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))