from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        '''
            나의 풀이
            2 ~ 9 까지의 숫자로 이루어진 문자열이 주어지면
            해당 숫자와 휴대폰 자판?으로 만들 수 있는 문자들의 모든 조합 구하는 문제

            미리 대응되는 숫자에 대한 문자표를 만들어두고
            재귀로 전부 만들어줌

            솔직히 모든 조합이라고 하길래 무조건 시간초과 뜰줄 알았는데
            보니까 최대 문자열의 길이가 4라서 그냥 통과하는듯??
        '''

        phone_str = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g','h','i'],
            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'], '9': ['w','x','y','z']
        }

        words = []

        # 현재 조합의 idx 정보들
        num_of_idx = [0] * len(digits)

        def makeWord(word_idx, num_of_idx, now_word):
            
            if word_idx == len(digits):
                return

            # 현재 위치의 숫자 문자표를 전부 넣어주기
            while num_of_idx[word_idx] < len(phone_str[digits[word_idx]]):
                word = phone_str[digits[word_idx]][num_of_idx[word_idx]]

                # 완성된 문자열이 조합해야하는 문자열의 길이일 경우 정답 배열에 넣기
                if len(now_word + word) == len(digits):
                    words.append(now_word + word)
                
                # 다음 문자로 넘어가기
                makeWord(word_idx + 1, num_of_idx, now_word + word)
                num_of_idx[word_idx] += 1

            # 첫번째 조합해야하는 문자가 아닌 경우 0으로 초기화
            if word_idx != 0:
                num_of_idx[word_idx] = 0
            
            return
        
        makeWord(0, num_of_idx, '')

        return words

    def firstSoul(self, digits: str) -> List[str]:

        '''
            책 풀이
            나랑 똑같이 문자표 만들어두고 재귀로 구현함
            근데 코드가 훨씬 깔끔하고 보기 좋음

            그나마 내가 잘한거라곤 시간복잡도 10ms? 정도랑 공간복잡도가 0.1mb 가 더 나옴 ㅋㅋㅋㅋ

            같은 원리를 하다고 하더라도 읽기 편한 코드를 작성하도록 
            노력하자..!
        '''

        result = []

        dic = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxzy'
        }


        if not digits:
            return []

        def dfs(index, path):

            # 이렇게 중간에 끝내는게 백트래킹이라고 할 수 있음
            # 문제상 사실상 끝난거지만
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)
        
        dfs(0, '')
        return result

obj = Solution()
print(obj.letterCombinations('23'))