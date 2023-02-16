from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        '''
            나의 풀이
            좌표평면에서 원점이랑 가장 가까운 점 k개를 반환하는 문제

            쉬웠음 ㅋㅋ
            그냥 유클리드 거리 계산해서 배열에 넣어주고
            계산된 거리를 기준으로 정렬
            그 다음 k 개를 반환하는 방식으로 구현
            
            근데 시간, 공간은 36%, 5% ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        '''

        dist_points = []
        for x, y in points:
            dist = ((x ** 2) + (y ** 2)) ** (1/2)
            dist_points.append([dist, x, y])

        dist_points.sort(key=lambda x: x[0])

        print(dist_points)

        return [[dist_points[i][1], dist_points[i][2]] for i in range(k)]

    
    def firstSoul(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        '''
            책 풀이
            heap 정렬 사용해서 품
            생각해보니 굳이 루트를 할 필요가 없었네? ㅋㅋㅋㅋ
            어차피 루트를 하든 말든 가장 작은 값이 가장 가까운 거리일테니 ㅋㅋㅋ

            전체적인 풀이는 나랑 비슷한데
            그냥 어떤 정렬을 했는지 차이 정도??

            근데 시간, 공간은 54%, 20%인데
            왜 차이나는거지?? ㅋㅋㅋ
            아 저거 print해서 그런듯 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
            print 지우고 다시하니까 80%, 20% ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
            앞으로 제출 할때 print 없애야 할듯
        '''

        heap = []

        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))
        
        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append([x,y])
        
        return result