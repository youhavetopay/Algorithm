import collections

class Solution:
    def getSum(self, a: int, b: int) -> int:

        '''
            나의 풀이(못품)
            +, - 연산을 사용하지 않고 두 수의 덧셈을 구현하는 문제
            이걸 어찌해 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ

            못품 ㅋㅋㅋㅋ
            비트연산 유형 문제이니까 비트 연산을 사용하면
            풀 수 있을 것 같은데....
            도저히 방법을 모르겠음..ㅠㅠ
        '''

        print(bin(a))
        print(bin(b))

        print(a | b)

        return
    
    def firstSoul(self, a: int, b: int) -> int:

        '''
            첫번째 책 풀이
            전가산기를 직접 구현함 ㅋㅋㅋㅋㅋㅋㅋㅋ

            문제가 너무 어려운듯...
            너무 깊다. ㅋㅋㅋㅋ
            문제를 풀려면 전가산기가 정확이 뭔지 알아야 구현이 가능할듯??
        '''
        
        # 2의 보수를 만들기 위한 비트마스크..
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        # 숫자 이진수로 변환하면서 전처리해주기
        # zfill 하면 해당 숫자만큼 0으로 채워줌
        # 데이터 입력 크기가 -1000 ~ 1000 까지라서 넉넉하게 32비트로 초기화
        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0
        sum = 0

        # 제일 뒤(가장 낮은 숫자)부터 계산
        for i in range(32):

            # 근데 이거 - 연산 아님..??? ㅋㅋㅋㅋ
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])

            # 전가산기 연산
            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            sum = carry ^ Q2
            carry = Q1 | Q3

            result.append(str(sum))
        
        # 마지막 연산까지 연산 후에 carry에 1이 남아 있으면
        # 자리수가 올라간거라서 1 붙여주기
        if carry == 1:
            result.append('1')
        
        # 결과를 뒤집어주고 10진수로 만들고 자리수가 넘었다면 마스킹해서 없애기
        result = int(''.join(result[::-1]), 2) & MASK

        # 음수 처리??
        if result > INT_MAX:
            result = ~(result ^ MASK)
        
        return result
    
    def secondSoul(self, a: int, b: int) -> int:
        
        '''
            두번째 책 풀이

            첫번째 풀이를 좀 간단하게..??? 푼 풀이법
            코드는 짧지만 이해 1도 안감 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        '''

        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            # a에는 carry 값을 고려하지 않은 a 와 b의 합이고
            # b에는 자릿수를 올려가며 carry값이 담기게 함????
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        
        if a > INT_MAX:
            a = ~(a ^ MASK)
        
        return a


obj = Solution()
print(obj.getSum(2, 3))
