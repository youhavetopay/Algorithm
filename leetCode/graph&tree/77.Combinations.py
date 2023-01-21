from typing import List
import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        '''
            나의 풀이
            일정 범위의 숫자들의 k개의 조합을 만드는 문제(중복은 제거)

            이전에 46.Permutations 문제랑 거의 비슷하다고 생각함
            하나하나 넣고 길이가 k개면 results에 담는 방법으로 품

            대신에 시간복잡도는 좀 걸리는듯? 상위 50퍼..ㅋㅋ
        '''

        results = []

        if n == k:
            temp = [i for i in range(1, n+1)]
            results.append(temp)
            return results

        def dfs(start, nums):
            if len(nums) == k:
                results.append(nums)
                return
            
            for i in range(start, n+1):
                dfs(i+1, nums + [i])

            return
        
        dfs(1, [])

        return results


    def firstSoul(self, n: int, k: int) -> List[List[int]]:

        '''
            첫번째 책 풀이
            나랑 거의 똑같음 ㅋㅋ
            근데 나보다 50ms빠름..?
            
            확실하지는 않지만 
            더하기 연산이랑 append 연산이랑 
            속도 차이가 있는듯함...?
        '''

        results = []

        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])
                return
            
            for i in range(start, n + 1):
                elements.append(i)

                dfs(elements, i + 1, k - 1)

                elements.pop()
        
        dfs([], 1, k)

        return results
    
    def secondSoul(self, n: int, k: int) -> List[List[int]]:
        
        '''
            두번째 책 풀이
            혹시나 했지만 역시나 itertools에 조합을 구해주는 모듈이 있었음 ㅋㅋ
            속도도 엄청 빠름

            위에 풀이가 대충 400ms정도 나오는데
            이거는 80ms 정도..ㄷㄷ

            책에 따르면 위에 풀이도 그렇게 효율적인 풀이는 아니라고 함
            이해를 위해 약간 비효율적으로 풀었다고 함

            k와 n을 뒤집어서 k-1 을 재귀호출 하는 방법으로 하면 더 효율적.....??????
            뭔소린지는 모르겠지만 더 효율적인 알고리즘이 있다고 함
        '''

        return list(itertools.combinations(range(1, n+1), k))

obj = Solution()
print(obj.combine(4, 3))