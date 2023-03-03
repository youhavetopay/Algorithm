from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
            나의 풀이
            주식을 사고 팔때 가장 많이 얻을 수 있는 이득을 구하는 문제

            배열을 순회하면서 이전 값에 비해 값이 올랐다면
            해당 차이를 저장하고
            마지막에 총합을 반환하면 됨

            medium이라길래 살짝 겁냈는데
            생각보다 쉬웠음,.??
        '''

        benefit_prices = [0]

        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                benefit_prices.append(prices[i] - prices[i-1])

        print(benefit_prices)

        return sum(benefit_prices)
    
    def secondMaxProfit(self, prices: List[int]) -> int:

        '''
            나의 두번째 풀이
            생각해보니 굳이 배열을 쓸 필요가 없어서 개선..?? 함
            그냥 더하면 되는 거 였음 ㅋㅋㅋㅋ
        '''

        max_benefit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                max_benefit += (prices[i] - prices[i-1])

        return max_benefit

    def firstSoul(self, prices: List[int]) -> int:

        '''
            첫번째 책 풀이
            나의 두번째 풀이랑 똑같음
            문제가 주식을 저점에 사서 고점에 파는 거라서 
            탐욕이라는 문제랑 가장 잘 어울린다고 함 ㅋㅋㅋㅋㅋㅋㅋㅋ
        '''

        result = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                result += prices[i+1]-prices[i]
        
        return result

    def secondSoul(self, prices: List[int]) -> int:
        
        '''
            두번째 책 풀이
            파이썬 다운 풀이
            풀이 방식은 첫번째 풀이랑 크게 다른건 없음
            그냥 코드가 파이썬 답게 바꿨다..?? 정도
        '''

        return sum(max(prices[i+1] - prices[0], 0) for i in range(len(prices)-1))