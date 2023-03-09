from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        '''
            못품 ㅜㅜㅜ

            문자열로 수식이 주어졌을 때 괄호를 할 수 있는 모든 경우의 수에 대한
            수식의 결과값들을 반환하는 문제

            단순히 조합이 아니라 괄호에 따라 계산 순서가 달라지기 때문에??
            너무 어려웠음
            문제 접근조차 못했다는게 너무 아쉬움...
        '''

        return
    
    def firstSoul(self, expression: str) -> List[int]:
        
        '''
            책 풀이
            분할정복으로 수식을 나누고 
            각각의 계산하면서 리스트에 넣는 방식으로 구현함..

            와 너무 어려움..ㅜㅜㅜ
        '''

        # 수식을 계산하는 함수
        def compute(left, right, op):
            results = []

            # left랑 right는 숫자로 이루어진 리스트
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            
            return results
        
        # 들어온 수식이 숫자만 있는 경우 -> 다 나눴을 때
        if expression.isdigit():
            return [int(expression)]
        
        results = []

        for index, value in enumerate(expression):
            # 수식을 순회하면서 연산자가 나오는 경우 나누기
            # 이렇게 하면 모든 경우의 수를 찾을 수 있음..
            # (나는 이걸 생각을 못했음...) 
            if value in '-+*':
                # 연산자를 기준으로 왼쪽 오른쪽 나누기
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])

                results.extend(compute(left, right, value))

        return results