import collections
from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        '''
            나의 풀이 (못품.. 시간초과..ㅠㅠ)

            문자열 A,B가 주어지면 B의 각각의 단어를 모두 포함하는 A의 최소 길이인
            부분 문자열을 찾는 문제

            열심히 도전했지만 시간초과로 못품 ㅠㅠ
            제일 처음 B의 문자들의 각각의 A에서의 위치를 찾고
            해당 위치를 시작으로 A에서 찾아가는 방식으로 풀려고 했으나
            B의 단어가 중복도 되고 길이도 최대 10^5 까지라서 못품 ㅋㅋ
        '''

        # B의 길이가 A의 길이보다 크면 없으니까 "" 리턴
        if len(t) > len(s):
            return ""

        find_word_idxs = []

        # B의 문자열의 위치 찾기
        for idx, word in enumerate(s):

            if word in set(list(t)):
                find_word_idxs.append(idx)
        
        word_idxs = []
        length = -1
        
        print(find_word_idxs)
        
        for i in range(len(find_word_idxs)):
            
            # B의 각각의 단어 개수 계산
            word_check = collections.Counter(t)

            for j in range(i, len(find_word_idxs)):

                # 부분문자열을 찾았었고 현재 문자열의 길이가 해당 길이보다 길면 끝내기                
                if word_idxs and length < (find_word_idxs[j] - find_word_idxs[i]):
                    break
                
                # 단어 체크
                word_check[s[find_word_idxs[j]]] = max(word_check[s[find_word_idxs[j]]]-1, 0)

                # B의 모든 단어를 찾은 경우
                # 위치 기록 및 길이 기록
                if not any(word_check.values()):
                    word_idxs = [find_word_idxs[i], find_word_idxs[j]]
                    length = find_word_idxs[j] - find_word_idxs[i]
                    break

            
        # 못찾았으면 "" 리턴
        if word_idxs == []:
            return ""
        
        return s[word_idxs[0] : word_idxs[1]+1]
    

    def firstSoul(self, s: str, t: str) -> str:
        
        '''
            첫번째 책 풀이(시간초과)

            이렇게 하면 안풀린다는 예제 임
            최소 윈도우 크기를 t의 길이로 해서
            하나씩 늘려가면서 s를 탐색하는 방법
            O(n^2)이라서 안풀린다고 함
        '''

        def contains(s_substr_lst:List, t_lst: List):
            for t_elem in t_lst:
                if t_elem in s_substr_lst:
                    s_substr_lst.remove(t_elem)
                else:
                    return False
            return True

        if not s or not t:
            return ''
        
        window_size = len(t)
        for size in range(window_size, len(s) + 1):
            for left in range(len(s) - size + 1):
                s_substr = s[left:left + size]
                if contains(list(s_substr), list(t)):
                    return s_substr
            
        return ''
    
    def secondSoul(self, s: str, t: str) -> str:

        '''
            두번째 책 풀이
            슬라이딩 윈도우를 활용한 풀이?

            필요한 총 문자의 개수랑 각각의 필요한 단어의 개수를 저장하고
            right를 시작으로 움직이면서 해당 단어를 빼줌
            그리고 필요한 문자 수가 0이라면 left를 움직이면서 음수가 아닐때까지 계속 증가시킴 -> 불필요한 단어까지 포함하고 있으니까
            그렇게 최소의 길이를 갱신하면서 반복
            어렵다 ㅋㅋ
        '''

        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        # enumerate([], n)은 n부터 시작하겠다는 것
        for right, char in enumerate(s, 1):
            
            # 이거는 저걸 만족하면 빼겠다는 뜻?
            # 즉 필요한 단어만 빼기 
            missing -= need[char] > 0
            need[char] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                if not end or right - left <= end - start:
                    start, end = left, right
                
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]

    def thirdSoul(self, s: str, t: str) -> str:

        '''
            세번째 풀이

            Counter를 사용해서 비교하는 방식 
            두번째 풀이보다 간단하지만 시간복잡도는 거의 30배 차이남 ㅋㅋㅋ 120ms -> 3300ms
            그래서 간단하게 풀수는 있지만 느려서 그냥 이런게 있다 정도..??

            & 연산을 하면서 비교를 해서 같으면 즉 필요한 문자들을 다 포함하고 있다면
            left를 당기면서 계속 확인하는 방법

        '''

        t_count = collections.Counter(t)
        current_count = collections.Counter()

        start = float('-inf')
        end = float('inf')

        left = 0
        for right, char in enumerate(s, 1):
            current_count[char] += 1

            while current_count & t_count == t_count:
                if right - left < end - start:
                    start, end = left, right
                
                current_count[s[left]] -= 1
                left += 1
        
        return s[start:end] if end - start <= len(s) else ''
        

obj = Solution()
print(obj.secondSoul("ADOBECODEBANC", "ABC"))