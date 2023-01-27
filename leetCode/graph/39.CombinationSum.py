from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        '''
            나의 풀이
            숫자들 중에서 합으로 target 만들 수 있는 숫자의 조합들 구하는 문제(숫자 중복 사용 가능)

            단순히 구하는건 쉬움 
            그냥 DFS로 전부 구하면 됨
            대신 중복 체크를 하는걸 어떻게 개선해야 할지 모르겠음
            예를들어서 7을 만들어야 한다 했을 때 
            내가 만든 알고리즘으로는 2, 2, 3이랑 2, 3, 2 이렇게 나오는데
            정답은 2,2,3 만 나오는거라서
            저런 중복을 없애야 함

            일단 풀었는데
            시간복잡도가 400ms 정도 나와서 좀 마음에 안듬 (하위 8%..)

            풀이는 마음에 안드는데 어떻게 해야할지 몰라서 책보기로 함..

        '''

        results = []

        dup_set = set()

        def dfs(nums):

            now_sum = sum(nums)

            if now_sum == target:
                
                sort_nums = sorted(nums)
                str_nums = ''.join(map(str, sort_nums))
                if str_nums not in dup_set:

                    results.append(nums)
                    dup_set.add(str_nums)

                return
            
            if now_sum > target:
                return

            for num in candidates:
                if now_sum + num <= target:
                    dfs(nums + [num])

        dfs([])

        return results

    def firstSoul(self, candidates: List[int], target: int) -> List[List[int]]:

        '''
            책 풀이

            뜨하..
            나랑 똑같은 원리임 -> DFS
            내 풀이는 순열을 구하는 풀이라서 저렇게 중복?? 이 생겼는데
            이 풀이는 조합을 구하는 풀이임
            그리고 문제는 조합을 구하는 문제임...

            조합인 경우에는 부모 인덱스를 볼 필요가 없어서 나의 위치부터 보면 됨
            그래서 index를 같이 넘겨줘서 거기서 부터 보면 훨씬 빠름!! 
            -> 이 풀이로는 50ms ㄷㄷ

            나의 풀이의 문제점은 조합을 구하는 문제에서 순열을 구해놓곤 
            거기서 중복이 있는걸 없애려고 하니 느렸던 거임
            중복을 체크하는게 문제가 아니라 애초에 탐색을 이상하게 했던 거임 -> for를 무조건 처음부터 시작했던 것
            
            어찌저찌 풀었지만 여전히 많이 부족한듯.. ㅋㅋ
        '''

        results = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            
            if csum == 0:
                results.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return results


obj = Solution()
print(obj.combinationSum([2,3,6,7], 7))