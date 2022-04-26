# 42. Trapping Rain Water
# 빗물 트래핑
# 난이도 : ★★★


# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
import sys
sys.setrecursionlimit(10**7)
from typing import List
def trap(height: List[int]) -> int:  # 내가 한 풀이 시간초과 ㅠㅠ O(n^2)??

    def findNextMaxValue(next_height, max_height_index, total_length, height, flag):  # 재귀함수로 돌림
        answer = 0

        # 왼쪽 혹은 오른쪽에 더이상 없을때
        if len(next_height) <= 1:
            return answer

        if flag: # 왼쪽일때
            max_height = max(next_height)  # 왼쪽에서의 최대값 찾기
            max_index = next_height.index(max_height) # 최대값의 인덱스 찾기
            for i in range(max_index+1, max_height_index): # 최대값의 인덱스 부터 이전 최대값 까지 
                answer += (height[max_index] - height[i]) # 현재 찾은 최대값에서 현재 높이 빼기 -> 채울 수 있는 빈칸
            answer += findNextMaxValue(height[:max_index], max_index, total_length, height, True) # 왼쪽으로 이동
        else:
            # 오른쪽일때
            max_value = 0
            max_index = -1
            for i in range(max_height_index + 1 , total_length): # 오른쪽에서의 최대값찾기
                if height[i] >= max_value:
                    max_index = i
                    max_value = height[i]
            
            for i in range(max_height_index +1, max_index): # 왼쪽연산과 동일
                answer += (max_value - height[i])
            answer += findNextMaxValue(height[max_index+1:], max_index, total_length, height, False) #오른쪽으로 이동

        return answer

    max_height = max(height)  # 제일 먼저 최대값 찾음

    max_index = height.index(max_height) # 최대값의 인덱스 찾음

    height_length = len(height)

    answer = 0
    
    # 최대값을 제외한 왼쪽에서의 최대값 찾기
    answer = findNextMaxValue(height[:max_index], max_index, height_length, height, True)
    
    # 최대값을 제외한 오른쪽에서의 최대값 찾기
    answer += findNextMaxValue(height[max_index+1:], max_index, height_length, height, False)

    

    return answer

# h1 = [0,1,0,2,1,0,1,3,2,1,2,1]
# h2 = [4,2,0,3,2,5]
# print(trap(h2))


def trap(height: List[int]) -> int: # 첫번째 풀이 투포인터 활용 O(n)
    if not height:
        return 0
    
    left, right = 0, len(height)-1 # 왼쪽 끝, 오른쪽 끝에서 시작
    left_max, right_max = height[left], height[right] # 현재 최대값 설정

    answer = 0

    while left < right: # 왼쪽이랑 오른쪽이랑 만나기 전까지
        left_max = max(left_max, height[left]) # 현재까지의 왼쪽에서의 최대값
        right_max = max(right_max, height[right]) # 현재까지의 오른쪽에서의 최대값

        if left_max <= right_max: # 오른쪽이 크다면 왼쪽을 이동
            answer += (left_max - height[left]) # 최대값과 현재 높이의 차이 더하기
            left += 1
        else: # 왼쪽이 더 크다면 오른쪽을 이동
            answer += (right_max - height[right]) # 위와 동일
            right += 1

    return answer


def trap(height: List[int]) -> int: # 두번째 풀이 STACK 활용 O(n)
    stack = []

    answer = 0


    # 높이 전체를 순회
    for i in range(len(height)):

        # 스택에 값이 있고 이전 위치의 높이보다 현재의 높이가 높을 때
        while stack and height[i] > height[stack[-1]]:

            # 이전 위치 빼기
            top = stack.pop()

            if not len(stack): # 스택이 비었을 때
                break

            # 이전과의 차이만큼 물높이 처리
            distance = i - stack[-1] - 1
            water = min(height[i], height[stack[-1]]) - height[top]

            answer += distance * water

        stack.append(i)

    return answer

h1 = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trap(h1))