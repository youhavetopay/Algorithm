from typing import List
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        '''
            나의 풀이
            리스트에서 원소를 모두 없애는데 걸리는 시간을 구하는 문제
            단 같은 원소는 n 번 기다린 후에 삭제 가능

            나의 접근법은 
            같은게 많이 남은 순으로 삭제하는 방식을 선택함

            파이썬에는 Counter라는 아주 좋은 기능이 있기에
            각각의 원소의 개수를 계산 한 다음 가장 많이 나온 n+1 개를 뽑아서
            하나씩 빼주는 방식으로 반복을 하고
            모든 원소가 없어질때까지 반복하는 방식으로 구현함

            솔직히 시간복잡도 걸릴줄 알았는데 바로 풀어서 의외였음 ㅋㅋ
        '''

        if n == 0:
            return len(tasks)
        
        counter = collections.Counter(tasks)

        time = 0

        while counter.values():

            print(counter.most_common(n+1))

            now_time = 0
            for key, _ in counter.most_common(n+1):
                counter[key] -= 1
                if counter[key] == 0:
                    del counter[key]
                now_time += 1
            
            if not counter.values():
                time += now_time
                break
            
            time += n+1


        return time
    
    def firstSoul(self, tasks: List[str], n: int) -> int:
        
        '''
            책 풀이

            우선순위 큐를 응용한 풀이법
            전체적으로 나랑 비슷한 풀이? 
            근데 counter 연산을 너무 많이 사용해서 시간 복잡도는 나보다 좀 더 걸림

        '''

        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1
                # subtract은 counter에서 task를 빼주는 역할
                counter.subtract(task)

                # 이렇게 하면 0인 counter는 없어짐
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        
        return result


obj = Solution()
print(obj.leastInterval(["A","A","A","B","B","B"], 2))