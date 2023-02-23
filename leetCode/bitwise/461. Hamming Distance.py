class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        '''
            나의 풀이
            두 숫자의 해밍거리 찾는 문제
            해밍거리는 문자가 다른 개수?? 정도??
            대충 이진수 다른거 개수??

            xor 연산해서 이진수로 만들고
            해당 이진수의 1의 개수를 세는 방법으로 품

            해밍거리랑 xor 연산만 알면 쉽게 푸는듯??
        '''

        temp = x ^ y

        answer = 0
        for word in bin(temp):
            if word == '1':
                answer += 1

        return answer
    
    def firstSoul(self, x: int, y: int) -> int:

        '''
            책 풀이
            나랑 똑같은 방법
            근데 count라는 함수를 사용함
            그래서 훨씬 깔끔한듯??
        '''

        return bin(x ^ y).count('1')


obj = Solution()
print(obj.hammingDistance(1,4))