import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
            나의 풀이
            s 의 단어를 재배치해서 t 문자가 되는지 확인하는 문제
            애너그램?? 가능한지 확인하는 문제

            엄청 쉬웠음
            푸는 시간보다 애너그램이 뭔지 확인하는게 더 시간이 오래걸린듯? ㅋㅋㅋㅋ

            dict으로 s의 각각의 단어의 개수를 체크
            그리고 t의 단어를 하나하나 체크하면서 하나씩 뺌 -> 전부 빼면 삭제
            만약 안들어 있으면 단어를 못만든 다는 소리니까 False
            마지막으로 반복이 끝났는데도 dict이 비어있지 않으면 False
            이렇게 품

            정렬문제라고 하는데 이걸 어떻게 정렬로 푸는거지???
        '''

        word_count = collections.defaultdict(int)

        for char in s:
            word_count[char] += 1
        
        for char in t:
            if char not in word_count:
                return False
            
            word_count[char] -= 1
            if word_count[char] == 0:
                del word_count[char]

        if len(word_count.keys()) != 0:
            return False

        return True
    
    def firstSoul(self, s: str, t: str) -> bool:

        '''
            책 풀이
            아.... ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
            정렬해서 그냥 비교하면 끝남 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
            어쩐지..easy 더라 ㅋㅋㅋ

            나 웰케 문제 어렵게 풀지..??

        '''

        return sorted(s) == sorted(t)