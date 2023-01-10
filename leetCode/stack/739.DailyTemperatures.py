from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        '''
            나의 풀이
            스택을 사용해서 품..? ㅋㅋ
            
            스택에 담을때 해당 날짜(인덱스)를 담아서 넣고
            나중에 체크할 때 top보다 온도가 높으면 빼고 날짜 계산

            스택에 담을 때는 
            스택이 비어있거나 top의 온도랑 같거나 낮을때 넣음
        '''

        # 정답 초기화(인덱스가 해당날짜)
        max_length = len(temperatures)
        wait_date = [0] * max_length

        stack = []

        for day, temper in enumerate(temperatures):
            
            while stack and stack[-1][1] < temper:
                temper_info = stack.pop()
                now_day = day - temper_info[0]
                wait_date[temper_info[0]] = now_day
            
            if not stack or (stack and stack[-1][1] >= temper):
                stack.append([day, temper])

        return wait_date
    
    def firstSoul(self, temperatures: List[int]) -> List[int]:

        '''
            책 풀이
            원리는 나랑 똑같음.. ㅋㅋㅋ 나이스!

            근데 코드가 더 우아함..ㅋㅋㅋ

            스택에 날짜(인덱스)만 넣어서 함

            인덱스만 넣고 굳이 넣을때 조건없이 넣어도 되는듯함
        '''

        wait_day = [0] * len(temperatures)
        stack = []

        for day, temper in enumerate(temperatures):

            while stack and temper > temperatures[stack[-1]]:
                last_day = stack.pop()
                wait_day[last_day] = day - last_day
            
            # 스택에 넣기
            stack.append(day)

        return wait_day


s = Solution()

print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))