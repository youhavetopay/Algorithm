from typing import List

import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        '''
            나의 풀이
            2차원 배열에서 target을 찾는 문제
            한 행, 열은 정렬되어 있음

            그냥 반복문 돌면서 범위에 있다면
            이진탐색을 하는 방법으로 품
            시간, 공간 이 그렇게 좋진 않음 39%, 32%
        '''

        for i in range(len(matrix)):

            if matrix[i][0] <= target <= matrix[i][-1]:
                target_idx = bisect.bisect_left(matrix[i], target)
                
                if target_idx < len(matrix[i]) and matrix[i][target_idx] == target:
                    return True
                
        return False
    
    def firstSoul(self, matrix: List[List[int]], target: int) -> bool:
        
        '''
            첫번째 책 풀이
            2차원 배열이 위 아래로는 정렬되어 있기 때문에
            현재 값이 target보다 작으면 한칸아래로, 크면 왼쪽으로 한칸
            이렇게 찾아가는 방식으로 구현함

            시간은 23% 지만 공간은 77%

            어떤 점에서 시작해서 차근차근 나아가는게 
            약간 길찾기 같아서 신기함 ㄷㄷ
            
        '''

        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
        
        return False
    
    def secondSoul(self, matrix: List[List[int]], target: int) -> bool:

        '''
            두번째 책 풀이
            데이터가 최대 300 x 300 이라서
            그냥 단순히 in으로 검사하는게 더 빠름...????? ㅋㅋㅋㅋ

            나도 처음에 데이터 크기 보고 in으로 할지 살짝 고민했는데
            그래도 문제가 이진탐색이니까 이진탐색 꾸역꾸역 넣었는데
            이게 더 효율적일지는 몰랐음 ㅋㅋㅋㅋㅋㅋㅋ

            시간 73%, 공간 77% ㄷㄷㄷ
        '''

        return any(target in row for row in matrix)

obj = Solution()
print(obj.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))