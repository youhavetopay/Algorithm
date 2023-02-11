from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        '''
            나의 풀이
            두개의 숫자로 이루어진 배열들이 주어졌을 때
            숫자의 범위가 겹치는 것은 하나로 묶는 문제
            ex) [1, 3], [2, 4] => [1, 4]

            먼저 입력값들을 정렬하고
            이전 start, end를 저장한 뒤
            이전 end와 현재 start, end와 비교해서 크면 갱신
            작으면 이전 start, end를 배열에 저장
            그리고 반복하는 방법으로 품

            그렇게 어렵진 않았는데
            시간, 공간 복잡도가 그렇게 좋지 않음 67%, 24%
            좀 더 획기적인 풀이가 있나??
        '''

        merge_datas = []

        pre_start, pre_end  = 0, 0

        for idx, (start, end) in enumerate(sorted(intervals, key=lambda x: x[0])):
            if idx == 0:
                pre_start, pre_end = start, end
                continue
            
            if pre_end >= start:
                if pre_end < end:
                    pre_end = end
            else:
                merge_datas.append([pre_start, pre_end])
                pre_start, pre_end = start, end

        merge_datas.append([pre_start, pre_end])
        print(merge_datas)


        return merge_datas
    
    def firstSoul(self, intervals: List[List[int]]) -> List[List[int]]:
        
        '''
            책 풀이
            역시 깔끔함 ㅋㅋ

            입력값을 정렬을 하고
            정답 배열의 마지막의 end와 현재 start를 비교
            마지막의 end가 크면 현재 end와 마지막의 end를 비교해서 큰 값을 넣고
            아니면 merged에 append하는 방식으로 구현

            시간 공간 복잡도가 엄청 좋음 => 97%, 99% ㄷㄷ
        '''
        
        merged = []

        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:

                '''
                    콤마 연산자
                    배열 더하기 할때 사용하는 거임
                    리스트 자체를 넣을때 사용하는 듯 함
                    ex)
                    a = [1,2,3]
                    b = [4,5] 

                    a += b => [1,2,3,4,5]

                    a += b, => [1,2,3,[4,5]]

                    a += [b] => [1,2,3,[4,5]]

                    append해도 통과는 하는데 
                    시간 공간 모두 낮게 나옴??
                    append보단 이게 더 좋은듯????
                '''
                merged += i,

        return merged

obj = Solution()
print(obj.merge([[1,4],[2,3]]))