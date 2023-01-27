from typing import List
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        '''
            나의 풀이
            숫자들의 순열을 구하는 문제

            주어지는 숫자들의 길이가 최대 6이라서
            그냥 dfs로 해도 상관 없을 것 같아서 이전 문제랑 비슷하게 품(17.LetterCombinationsofaPhoneNumber)

            처음에 문제를 봤을 때 당황해서 조금은 오래 걸림
        '''

        answers = []

        def dfs(fix_idxs):
            if len(fix_idxs) == len(nums):
                find_nums = []
                for idx in fix_idxs:
                    find_nums.append(nums[idx])
                answers.append(find_nums)
                return

            for i in range(len(nums)):
                if i not in fix_idxs:
                    dfs(fix_idxs + [i])


            return

        
        dfs([])

        return answers

    def firstSoul(self, nums: List[int]) -> List[List[int]]:

        '''
            첫번째 책 풀이
            순열의 상태?를 그래프로 나타내어
            리프노드에 갔을 경우 결과 리스트에 추가하는 방법으로 구현함
        '''

        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        
        dfs(nums)

        return results
    
    def secondSoul(self, nums: List[int]) -> List[List[int]]:
        '''
            두번째 책 풀이
            파이썬 다운 풀이 ㄷㄷ
            itertools 에 순열을 구해주는 모듈이 있다고 함
            대신에 튜플형태로 반환하기에 문제에서는 리스트 형태를 요구하기 때문에
            리스트로 변환을 해줘야 한다고 함
        '''
        return list(map(list, itertools.permutations(nums)))
    