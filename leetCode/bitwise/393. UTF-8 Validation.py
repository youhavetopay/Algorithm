from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:


        '''
            나의 풀이
            숫자 리스트가 주어지면 해당 숫자들이 UTF-8 을 만족하는지 체크하는 문제

            전부 8비트 이진수로 바꾼 다음
            시작 숫자를 찾아서
            그 뒤에 숫자들이 만족하는지 체크하는 방법으로 품

            시간, 공간 35%, 6% ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

            비트연산 유형의 문제라고 하긴 하는데
            일단 이렇게 풀어봄 ㅋㅋㅋㅋ

            좀 무식했지만 풀려서 그나마 다행??

            비트연산 문제가 많이 어려움...
        '''

        bin_datas = []

        for num in data:
            bin_datas.append(bin(num)[2:].zfill(8))

        print(bin_datas)

        idx = 0
        bit_count = -1
        while idx < len(bin_datas):

            for i, bit in enumerate(bin_datas[idx]):
                if bit == '0':
                    bit_count = i-1
                    break
            else:
                return False
            
            if bit_count == -1:
                idx += 1
                continue
            
            if bit_count == 0 or bit_count >= 4:
                return False



            check_count = 0
            idx += 1
            while idx < len(bin_datas) and check_count != bit_count:
                print(bin_datas[idx], check_count, bit_count)
                if bin_datas[idx][:2] == '10':
                    check_count += 1
                elif check_count != bit_count:
                        return False
                idx += 1
            
            print(check_count, bit_count)
            if check_count != bit_count:
                return False

            
        return True

    def firstSoul(self, data: List[int]) -> bool:

        '''
            책 풀이
            푸는 방식은 나랑 똑같음
            
            근데 비트 연산을 이용한 거랑
            데이터를 체크하는 부분을 함수로 따로 빼서 확인한거랑
            차이점이 있음

            그리고 무엇보다 코드가 훨~~~~~~~~~~씬 깔끔함 ㄷㄷㄷㄷ
        '''

        def check(size):

            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False

            return True
        
        start = 0
        while start < len(data):
            first = data[start]

            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        
        return True

obj = Solution()
print(obj.validUtf8([32,196,147,225,184,165,246,149,170,129,204,153,243,188,141,147,0,217,149,234,176,176,243,178,133,144,213,181,193,187,238,137,134,218,155,33,231,134,162,243,184,144,131,71,201,131,244,133,189,140,242,178,128,156,207,154,230,165,181,240,181,134,180,227,129,199,172,226,158,164,214,183,224,137,141,20,194,188,232,177,151,242,157,180,153,200,189,239,153,186,240,153,181,154]))