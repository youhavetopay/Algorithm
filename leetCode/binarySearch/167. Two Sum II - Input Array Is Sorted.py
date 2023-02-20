from typing import List

import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        '''
            나의 풀이
            정렬된 리스트에서 더해서 target이 되는 조합 찾는 문제

            처음에 이중 for 문으로 풀었는데 시간초과 떠서
            어차피 정렬된 리스트니까 첫번째 요소는 차례대로 찾고
            두번째 요소는 이진탐색으로 찾는 방법으로 품

            어찌저찌 풀었는데 시간복잡도가 17%....ㅋㅋ
        '''

        for i in range(len(numbers)):
            
            start, end = i+1, len(numbers)-1
            new_target = target - numbers[i]

            while start <= end:
                mid = start + (end - start) // 2

                if numbers[mid] < new_target:
                    start = mid + 1
                elif numbers[mid] > new_target:
                    end = mid - 1
                else:
                    return [i+1, mid+1]


        return
    
    def firstSoul(self, numbers: List[int], target: int) -> List[int]:
        
        '''
            첫번째 책 풀이
            투포인터를 통해 품..
            으아 투포인터라니.. 좀 더 열심히 해야할 듯..ㅋㅋㅋ

            정렬된 리스트니까 처음이랑 끝에서 부터 차례대로 더하면서
            더한 값이 작으면 왼쪽 + 1, 크면 오른쪽 - 1 하는 방식으로 품
            이렇게 하니까 시간복잡도 42% 가 나옴
        '''

        left, right = 0, len(numbers)-1

        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1
    
    def secondSoul(self, numbers: List[int], target: int) -> List[int]:

        '''
            두번째 책 풀이
            나랑 똑같은 풀이
            순차적으로 첫번째 요소를 찾고 두번째요소는 이진탐색으로 찾는 방법
        '''

        for k, v in enumerate(numbers):
            left, right = k+1, len(numbers)-1

            expected = target - k

            while left <= right:
                mid = left + (right - left) // 2

                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k+1, mid+1

        return
    
    def thirdSoul(self, numbers: List[int], target: int) -> List[int]:
        
        '''
            세번째 책 풀이
            두번째 풀이에서 이진탐색을 bisect 모듈을 사용해서 품
            대신 슬라이싱 연산 때문에 시간복잡도가 엄청 아슬아슬함.. 5%
        '''

        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k+1:], expected)

            if i < len(numbers[k+1:]) and numbers[i+k+1] == expected:
                return k+1, i+k+2
    
    def fourthSoul(self, numbers: List[int], target: int) -> List[int]:

        '''
            네번째 책 풀이
            세번째 풀이 개선편
            해봤자 슬라이싱 연산 한번으로 줄인거
            대신 시간복잡도는 절반으로 줄어듬 약 4000ms -> 2000ms 정도?? 그래도 5%..
        '''

        for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k+1:]
            i = bisect.bisect_left(nums, expected)

            if i < len(nums) and numbers[i+k+1] == expected:
                return k+1, i+k+2
    
    def fifthSoul(self, numbers: List[int], target: int) -> List[int]:

        '''
             다섯번째 책 풀이
             슬라이싱 연산 대신
             bisect의 범위를 줄이는 인자를 넣어줌
        '''

        for k, v in enumerate(numbers):
            expected = target - v
            
            i = bisect.bisect_left(numbers, expected, k+1)

            if i < len(numbers) and numbers[i] == expected:
                return k+1, i+1