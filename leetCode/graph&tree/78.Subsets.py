from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        '''
            나의 풀이
            중복되지 않은 숫자들에서 부분조합을 구하는 문제

            쉬웠음 39.CombinationSum 문제의 책 풀이랑 비슷하게 품
            근데 시간복잡도가 하위 33퍼라서 좀 그럼..

            dfs로 풀었고 조합을 구하는거니까
            나 다음부터 탐색하도록 함 -> 중복제거
            특이하게 빈배열도 부분조합이라고 해야해서 미리 넣어줌
            그리고 예제 출력의 순서랑 달라도 정답이 인정됨 !!

            39번 문제랑 비슷하게 어렵지 않게 풀었지만 
            최적화를 어떻게 해야할지 모르겠어서 
            책봐야겠음.. ㅠㅠ
        '''
        
        results = [[]]

        def dfs(index, subset):
            for i in range(index, len(nums)):
                temp = subset + [nums[i]]
                results.append(temp)
                dfs(i + 1, temp)

        dfs(0, [])

        return results
    
    def firstSoul(self, nums: List[int]) -> List[List[int]]:

        '''
            책 풀이
            나랑 똑같음...
            results에 넣는 순서만 다르고 같음

            근데 왜 시간, 공간복잡도가 차이가 나지...????
            넣는 순서가 그렇게 상관이 있나..??
            20ms 차이 이긴 한데....
            씁......

            어쨌든 간에 책 코드가 훨씬 깔끔하고 초기값 설정도 간편하니
            책 풀이가 더 좋은듯
        '''

        results = []

        def dfs(index, path):
            results.append(path)

            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])

        return results


obj = Solution()
print(obj.subsets([1,2,3]))