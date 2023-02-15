from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
            나의 풀이
            제자리 정렬하는 문제

            데이터 크기가 300까지라서 그냥 버블정렬로 품
            그래서 그런지 시간복잡도가 16% ㅋㅋㅋㅋㅋ
        '''

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]

        print(nums)

        return
    
    def firstSoul(self, nums: List[int]) -> None:

        '''
            책 풀이
            네덜란드 국기 문제?? 라고 함
            일반적인 정렬을 하기 보단 값이 0, 1, 2 밖에 없으므로
            좀더 효율적인 정렬이 가능하다고 함

            퀵정렬을 개선시킨 버전 정도??
            red는 0, white는 1, blue는 2를 기준으로 정렬

            대충 red은 왼쪽, blue는 오른쪽에서 white가 움직이면서
            계속 값에 따라 위치를 이동시키는 방식으로 정렬

            나의 풀이랑 시간복잡도가 거의 2배 차이남 ㅋㅋㅋ
        '''

        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[blue], nums[white] = nums[white], nums[blue]
            else:
                white += 1

        return

        


obj = Solution()
print(obj.sortColors([2,0,2,1,1,0]))