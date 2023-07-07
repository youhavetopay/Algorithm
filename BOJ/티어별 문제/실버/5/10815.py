
'''
    백준 10815. 숫자 카드
    주어진 숫자 배열에 해당 숫자가 있는지 없는지 체크하는 문제
'''

import sys
input = sys.stdin.readline

'''
    나의 풀이

    나의 접근법
    숫자 개수가 많길래
    이진탐색으로 해보니까 통과함 ㅋㅋ
'''

def binary_search(target, nums, length):

    left = 0
    right = length - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return 1
    
    return 0

# N = int(input())
# sang_card = list(map(int, input().split()))

# M = int(input())
# check_nums = list(map(int, input().split()))

N = 5
sang_card = [6, 3, 2, 10, -10]

M = 8
check_nums = [10, 9, -5, 2, 3, 4, 5, -10]

sang_card.sort()

answers = []
for target in check_nums:
    answers.append(binary_search(target, sang_card, N))

print(' '.join(map(str, answers)))


def my_second_solu():

    '''
        나의 두번째 풀이

        이거 그냥 있는지 없는지만 검사하면 되니까
        set에다가 담아서 in으로 체크함
        이렇게 하니까 이진탐색보다 3배 빠름 ㅋㅋㅋㅋㅋㅋㅋㅋ
        메모리는 좀 더쓰긴 했는데
        3배는 빨라서..

        아니 그리고 2년전에 나는 이걸 못풀었다고?? 
        진짜 심각하다...
        그때는 탐색에 대한 시간복잡도 개념이 많~~~~~~~~~이 부족한 것 같음.. ㅋㅋㅋ
    '''

    N = int(input())
    sang_card = set(list(map(int, input().split())))

    M = int(input())
    check_nums = list(map(int, input().split()))

    answers = []
    for target in check_nums:
        if target in sang_card:
            answers.append(1)
        else:
            answers.append(0)

    print(' '.join(map(str, answers)))




def firstSolu():

    '''
        다른 사람 풀이
        https://wlstyql.tistory.com/154

        이분은 dict 자료형으로 체크함
        dict 자료형이나 set 이나 in 복잡도는 똑같아서
        자기 하고 싶은걸로 하면 될듯? ㅋㅋ
        그리고 정답을 출력할때 굳이 배열에 담아서 다시 join으로 하는 것 보단
        저렇게 print로 바로 하는게 훨씬 좋을듯 함
    '''

    N = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    checks = list(map(int, sys.stdin.readline().split()))

    _dict = {}  # 속도는 dictionary!
    for i in range(len(cards)):
        _dict[cards[i]] = 0  # 아무 숫자로 mapping

    for j in range(M):
        if checks[j] not in _dict:
            print(0, end=' ')
        else:
            print(1, end=' ')