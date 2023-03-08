from typing import List
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        '''
            나의 풀이
            
            리스트에 숫자들 중 가장 많이 있는 숫자를 찾는 문제

            이렇게 풀어도 되나.. ㅋㅋㅋㅋ
            Counter로 각각의 개수를 계산하고 most_common으로 찾아서 반환 ㅋㅋㅋ

            알고리즘에는 정답이 없는거니까
            이렇게 해도 상관은 없겠지만....
        '''

        return collections.Counter(nums).most_common(1)[0][0]
    
    def firstSoul(self, nums: List[int]) -> int:
        
        '''
            첫번째 책 풀이(시간초과)

            문제에서 무조건 가장 많은건 과반수 이상이라고 했으니
            하나하나 count해서 과반수를 넘어가는 걸 찾아가는 방식의 풀이
            중복된 요소도 많고 길이도 5*10^4 까지라서 시간초과 뜸
        '''

        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num

    def secondSoul(self, nums: List[int]) -> int:
        
        '''
            두번째 책 풀이

            첫번째 풀이를 최적화 했음
            한번 count한 숫자는 다시 계산 안하도록 dict에 계산값을 저장해둠
            
            이렇게 계산한 걸 저장해두는 걸 메모제이션이라고 하는데
            DP에서 중요한 개념 중 하나이니까 잘 익혀둬야 할듯..??
        '''

        counts = collections.defaultdict(int)

        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            
            if counts[num] > len(nums) // 2:
                return num
        
    def thirdSoul(self, nums: List[int]) -> int:

        '''
            세번째 책 풀이

            분할정복을 사용한 풀이법
            리스트를 절반으로 계속 나눔(분할)

            그리고 전부 나눈 다음 해당 리스트에서 count를 체크
            count가 높은 숫자가 올라감(정복?ㅋㅋ)
            
            가장 많은 숫자가 절반 이상을 차지한다고 했으니
            무조건 정답이 나온다고 함..(비둘기집 원리????)

        
            코드도 디게 깔끔하고 좋지만
            시간복잡도는 좋지 않음 내 풀이의 거의 2배?? 차이남

        '''

        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]
    
    def fourthSoul(self, nums: List[int]) -> int:

        '''
            네번째 책 풀이
            
            정렬을 하면 리스트의 가운데는 무조건 최빈도 수이기 때문에
            가능한 풀이 ㅋㅋㅋ
            파이썬 다운 풀이라고 함 ㅋㅋㅋ
            이 풀이가 모든 풀이 통틀어서 가장 시간, 공간 모두 좋음 
        '''

        return sorted(nums)[len(nums) // 2]