from typing import List
import collections
import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        '''
            나의 풀이(시간초과..)
            2차원 배열을 규칙에 맞게 재정렬하는 문제

            나의 접근법
            나보다 큰사람의 수와 나의 키를 기준으로 정렬
            현재 정렬된 사람의 수를 시작으로
            들어올 수 있는 사람들 체크함

            들어올 수 있는 사람은 정렬된 사람들 중 
            나보다 큰 사람의 수를 만족하면서
            그 중 가장 키가 작은 사람을 우선으로 넣기
            
            접근법 자체가 잘못된 건지 
            시간초과가 뜸 ㅋㅋ
            그리디 하게 풀었긴 한데 너무 비효율적인듯..
        '''

        answer_queue = []
        height_table = collections.defaultdict(list)
        
        people.sort(key=lambda x:(x[1], -x[0]))
        print(people)

        for height, count in people:
            height_table[count].append(height)

        total_length = len(people)
        while len(answer_queue) < total_length:
            max_count = len(answer_queue)

            while max_count >= 0:
                
                if height_table[max_count]:
                    check_height = height_table[max_count][-1]
                    now_count = 0
                    for height, _ in answer_queue:
                        if height >= check_height:
                            now_count += 1
                        
                        if now_count > max_count:
                            break
                

                    if now_count == max_count:
                        answer_queue.append([height_table[max_count].pop(), max_count])
                        break
                elif height_table[max_count] == []:
                    del height_table[max_count]
                    

                max_count -= 1

        return answer_queue
    
    def firstSoul(self, people: List[List[int]]) -> List[List[int]]:

        '''
            책 풀이 
            ㅋㅋㅋㅋ 우선순위 큐를 통해 품

            나보다 큰 사람의 수는 인덱스로 하고
            최대 힙을 사용해서 키가 가장 큰 사람 부터 배열에 insert
            
            그리디 문제는 대부분 우선순위 큐를 많이 활용한다고 하니
            알아두자....ㅋㅋㅋㅋ

        '''

        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        
        result = []
        while heap:
            person = heapq.heapop(heap)
            result.insert(person[1], [-person[0], person[1]])

        return result

obj = Solution()
print(obj.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))