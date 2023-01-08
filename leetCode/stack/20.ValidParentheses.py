class Solution:
    def isValid(self, s: str) -> bool:
        '''
            괄호 검사 문제
            개인적으로 이런 문제만 한 5번 푼듯 ㅋㅋㅋㅋㅋ

            문자 순회하면서 스택에 열린괄호 담고
            닫힌 괄호 나오면 top에 있는거 검사하는 방식으로 구현
        '''

        stack = []

        bracket_info = [['(', ')'], ['{', '}'], ['[', ']']]

        for word in s:
            if word == '(' or word == '{' or word == '[':
                stack.append(word)
            else:

                if stack == []:
                    return False
                
                for bracket in bracket_info:
                    if word == bracket[1]:
                        if stack[-1] != bracket[0]:
                            return False
                        stack.pop()
                        break
                else:
                    return False

        if stack != []:
            return False

        return True
    
    def firstSoul(self, s: str) -> bool:
        
        '''
            책 풀이
            방식은 똑같음

            근데 코드가 와우 ㅋㅋ
            dict 자료형으로 테이블 매칭
        '''

        stack = []
        table = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for word in s:
            if word not in table:
                stack.append(word)
            elif not stack or table[word] != stack.pop():
                return False
        
        return len(stack) == 0