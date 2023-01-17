from typing import List
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
            나의 풀이
            가장 많이 중복된 숫자 k 개 반환하는 문제

            저번에 봤던 collections.Counter 사용해서 각각의 갯수를 구한 다음
            value를 기준으로 내림차순으로 정렬

            그 다음 k개 만큼 반환

            Counter 덕분에 코드가 짧아진듯?
            안그랬으면 배열 돌면서 dict에 담았을꺼니까..
        '''

        counter = collections.Counter(nums)

        sort_nums = sorted(counter.items(), key= lambda x: x[1], reverse=True)

        top_Ks = []
        for i in range(k):
            if i == len(sort_nums):
                break
            top_Ks.append(sort_nums[i][0])

        return top_Ks
    
    def firstSoul(self, nums: List[int], k: int) -> List[int]:
        '''
            첫번째 책 풀이
            Counter를 사용한건 나랑 같음
            대신 리스트를 정렬하는 것이 아닌
            heap에 넣어서 함 빈도수는 -로 해서 최소값이 되도록 함

            heap 정렬을 하든 sorted를 사용하든 그 차이인듯??
            나의 풀이랑 시간복잡도랑 공간복잡도도 비슷함
        '''

        fregs = collections.Counter(nums)
        heap = []

        for f in fregs:
            heapq.heappush(heap, (-fregs[f], f))
        
        answer = list()
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])

        return answer
    
    def secondSoul(self, nums: List[int], k: int) -> List[int]:
        '''
            두번째 책 풀이
            파이썬 다운 풀이 ㄷㄷㄷㄷ

            Counter에 most_common이라는 빈도수가 높은 순서대로 추출하는 함수가 있음
        '''

        return list(zip(*collections.Counter(nums).most_common(k)))[0]


obj = Solution()
print(obj.topKFrequent([1,1,1,2,2,3], 2))