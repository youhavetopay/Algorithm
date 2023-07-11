
'''
    백준 1107. 리모컨

    현재 채널의 100번 채널이고
    고장난 채널 버튼이 있을때
    최소로 몇번 눌러야 목표 채널로 가는지 계산하는 문제

'''
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

wrong_buttons = []
if M > 0:
    wrong_buttons = list(map(int, input().split()))
    
# N = 500000
# M = 6
# wrong_buttons = [0, 1, 2, 3, 4, 5]

can_push_buttons = []

for i in range(0, 10):
    if i not in wrong_buttons:
        can_push_buttons.append(i)

min_push_count = abs(N - 100)

def solution():

    '''
        나의 풀이

        나의 접근법
        처음엔 예전에 프로그래머스에서 풀었던 엘리베이터 문제랑
        비슷한 것 같아서 해보려고 했는데 좀 달랐음
        엘리베이터 문제는 10^N 단위로 움직일 수 있지만
        여기서는 버튼이 고장나지만 않았다면 바로 해당 채널로 갈 수 있어서 
        유형이 조금 다른 것 같음

        그래서 생각한게
        3가지 방향으로 접근해보려고 했음
        1. 1채널씩 움직일 수 있는 버튼으로만 이동하기
        2. N 보다 큰 수 중에서 최대값(채널 숫자 버튼으로 이동) 으로 간 후 1채널씩 내리기
        3. N 보다 작은 수 중에서 최소값(채널 숫자 버튼으로 이동) 으로 간 후 1채널씩 올리기

        이렇게 구해보려고 했는데
        N의 최대값이 50만 이라서 
        만들 수 있는 최소 중의 최대값과 최대 중의 최소값을 찾는게 너~~~~~~~무 어려웠음
        스택으로도 해보고, 뒤집어서 거꾸로 찾아보고 별짓을 다했는데
        반례를 돌려보니 하나같이 다 틀림 ㅋㅋㅋ

        그렇게
        최대값이 50만 이라서 처음엔 모든 조합을 찾지 못한다고 생각했으나
        다시 생각해보니 50만의 자리수는 최대 6자리 라서 충분히 숫자 조합을 찾을 수 있다 라는 생각이 들었고
        해보니 통과.... 


        진짜 너무 어려웠음
        솔직히 골드 5를 못푼다는게 너무 억울해서
        진짜 2일동안 풀었음 ㅠㅠㅠㅠㅠㅠㅠㅠㅠ
        그리고 너무 허무함
        내가 진짜 골드는 못푸는 실력인 줄 알았는데
        접근을 잘못했던 거였음....

        다음 부터는 문제 제한 사항에 대해 좀 더 자세히 살펴보자.. ㅋ

    '''

    global N, M, min_push_count
    
    # 이동해야 하는 채널이 현재 채널인 경우
    if N == 100:
        return 0
    
    # 누를 수 있는 채널 버튼이 없는 경우
    if len(wrong_buttons) == 10:
        return abs(100 - N)

    # 최소 중의 최대값
    min_max_num = -sys.maxsize

    # 최대 중의 최소값
    max_min_num = sys.maxsize
    numbers = list(map(int, str(N)))

    
    count = 0
    for num in numbers:
        if int(num) in can_push_buttons:
            count += 1

    # 이동하려는 채널의 자리수의 숫자가
    # 모두 누를 수 있는 버튼일 때
    if count == len(numbers):
        return min(count, min_push_count)
    
    total_nums = []

    # 누를 수 있는 버튼으로 만들 수 있는 채널들 찾기 -> 목표 채널의 자리수와 동일한 숫자 찾기
    def dfs(now):
        if len(now) == len(numbers):
            total_nums.append(now)
            return
        
        for num in can_push_buttons:
            dfs(now + [num])
    
    dfs([])

    # 최소값과 최대값 찾기
    for nums in total_nums:
        
        num = int(''.join(map(str, nums)))

        if num > N:
            max_min_num = min(max_min_num, num)

        if num < N:
            min_max_num = max(min_max_num, num)

    # 해당 자리수에 만족하는 최대 중 최소 값이 없을 때
    # 자리수 하나 높은 수에서 최소 값 만들기
    if max_min_num == sys.maxsize:

        # 누를 수 있는 버튼의 첫번째 값이 0이 아니면
        # 누를 수 있는 버튼은 정렬되어 있으므로 최소값 으로 목표채널의 자리수 + 1 로 구성하기
        if can_push_buttons[0] != 0:
            max_min_num = int(str(can_push_buttons[0]) * (len(numbers) + 1))
        
        # 누를 수 있는 버튼의 최소값이 0이고 개수가 2개 이상이면
        # 2번째 버튼을 맨앞자리로 하고 나머지를 0으로 채우기
        elif len(can_push_buttons) >= 2:
            max_min_num = int(str(can_push_buttons[1]) + (str(can_push_buttons[0]) * (len(numbers))))
    
    # 해당 자리수에 만족하는 최소 중 최대값이 없을 때
    # 자리수 하나 낮은거에서 최대값 만들기
    if min_max_num == -sys.maxsize:
        # 누를 수 있는 버튼이 0 만 있는게 아닐 때
        if can_push_buttons[-1] != 0:
            # 이동하려는 채널이 1자리수 가 아닐때
            if len(numbers) != 1:
                min_max_num = int(str(can_push_buttons[-1]) * (len(numbers) - 1))
            else:
                # 한자리수 수면 못만듬
                min_max_num = sys.maxsize
        else:
            # 누를 수 있는 버튼이 0밖에 없으면 최소 수 못만듬
            min_max_num = sys.maxsize

    # 3가지 경우의 최소 값 찾기
    return min(min_push_count, abs(N - min_max_num) + len(str(min_max_num)), abs(N-max_min_num)+ len(str(max_min_num)))


print(solution())


def firstSolu():

    '''
        다른 사람 풀이
        https://seongonion.tistory.com/99

        진짜 완전탐색으로 품
        0 ~ 100만까지 탐색을 하는데
        해당 채널을 버튼으로 이동할 수 있는 경우
        비교를 하면서 최소 값을 찾아감
        100백만 까지 하는 이유는
        목표 채널의 최대값이 50만이라고 해도
        버튼으로 만들 수 있는 수는 최대 100만이기 때문임
        
        ex) target = 50만, 누를 수 있는 버튼이 9, 5밖에 없을때
            100 -> 500_000
            955_555 -> 500_000 -> 이게 더 빠름

        근데 이거 시간복잡도가 300만이기 때문에
        좀 오래 걸리긴 함 시간도 2900ms 걸림 ㅋㅋ

        근데 신기한건 내가 계산한 시간복잡도가 얼추 300만 이라고 계산했는데
        걸리는 시간도 얼추 비슷해서 당연한 거지만 신기하긴 했음 ㅋㅋ
    '''

    target = int(input())
    n = int(input())
    broken = list(map(int, input().split()))

    min_count = abs(100 - target)

    for nums in range(1_000_001):
        nums = str(nums)

        for j in range(len(nums)):
            if int(nums[j]) in broken:
                break
            elif j == len(nums) - 1:
                min_count = min(min_count, abs(int(nums) - target) + len(nums))

    print(min_count)