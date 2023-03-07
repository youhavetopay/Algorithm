from typing import List
import bisect

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        '''
            나의 풀이
            두개의 리스트에서
            s 리스트를 기준으로 g에서 같거나 낮은 수의 개수를 계산하는 문제

            그냥 완전탐색으로 품
            둘다 정렬한 다음
            끝에서 부터 체크
            같거나 낮으면 둘다 -1 하고 개수 카운팅
            크면 g의 인덱스를 -1 하는 방식으로 품

            역시 easy라서 좀 쉬운듯 ㅋㅋ
        '''

        result = 0

        g_idx = len(g)-1
        s_idx = len(s)-1

        g.sort()
        s.sort()

        while s_idx >= 0 and g_idx >= 0:

            if g[g_idx] <= s[s_idx]:
                result += 1
                g_idx -= 1
                s_idx -= 1
            else:
                g_idx -= 1

        
        return result
    
    def firstSoul(self, g: List[int], s: List[int]) -> int:
        
        '''
            첫번째 책 풀이
            
            나의 풀이랑 거의 똑같음
            대신 정렬해서 0부터 시작한게 차이점이 있음
            
        '''


        g.sort()
        s.sort()

        child_i = cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            
            cookie_j += 1

        return child_i

    def secondSoul(self, g: List[int], s: List[int]) -> int:

        '''
            두번쨰 책 풀이
            이진탐색을 활용한 풀이

            s를 기준으로 순회하면서 g에서 이진탐색으로 찾음
            찾은 인덱스가 현재 쿠키를 준 아이들보다 클 경우 
            쿠키를 더 줄수 있기 때문에 +1
        '''

        g.sort()
        s.sort()

        result = 0
        for i in s:
            # g에서 i 보다 더 큰 인덱스 찾기
            index = bisect.bisect_right(g, i)

            if index > result:
                result += 1
        
        return result