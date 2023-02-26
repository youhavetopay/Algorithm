class Solution:
    def hammingWeight(self, n: int) -> int:

        '''
            나의 풀이
            이진수의 1의 개수를 반환하는 문제

            그냥 이진수로 변환하고 1의 개수를 계산하는 방식으로 품
            원래 이런 문제인가..??ㅋㅋㅋ
            난이도가 easy 이긴 한데...
        '''

        return bin(n)[2:].count('1')
    
    def fristSoul(self, n: int) -> int:

        '''
            첫번째 책 풀이
            나랑 똑같은 풀이임
            대신 슬라이스를 안한건데
            생각해보니 0bxxxxx ~~ 이렇게 변환되고
            1의 개수만 카운팅하면 되는거라서 굳이 안해도 되는 듯
            슬라이스 안하니까 시간복잡도 엄청 좋아짐 -> 41% => 95%
        '''

        return bin(n).count('1')

    def secondSoul(self, n: int) -> int:
        
        '''
            두번째 책 풀이
            첫번째 풀이는 파이썬에서 제공하는 문자열 처리 방법이라서
            비트연산자를 활용한 풀이법임

            n과 n-1 을 & 를 하면 비트가 한개 씩 빠짐
            그래서 0이 될때까지 계속 반복하면서 횟수만 카운팅 하면 됨
        '''

        count = 0

        while n:
            n &= n-1
            count += 1
        
        return count