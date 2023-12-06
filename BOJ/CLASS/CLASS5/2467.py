
'''
    백준 2467. 용액
    정렬된 배열에서 두 수의 합의 절대값이 0이랑 
    가장 가까운 수 두개를 찾는 문제
'''

import sys
import bisect

input = sys.stdin.readline


def solution():
    
    '''
        나의 풀이
        처음에 완전탐색으로 하려고 했는데
        생각해보니 배열 크기가 최대 20만이라서
        완전 탐색으로 하니까 시간초과가 떴음

        그래서 생각하다가 그냥 문제 유형을 봤는데
        이진탐색이랑 투포인터 길래 

        투포인터 방식으로 해봤는데 틀렸습니다가 떴음..
        투포인터로 처음과 끝부터 이전값이랑 비교하면서 
        left랑 right를 이동시키는 방법으로 했는데 이동시키는 조건이 확실하지 않아서
        실패함..

        그러다가 정렬된 값이 주어지므로 이진탐색을 생각해봤는데
        나를 기준으로 절대값이 나랑 같은 수가 가장 우선순위가 높으니
        그걸 찾고 거기서 기준으로 위아래로 탐색하는 방식으로 하니까 풀림 ㅋㅋ

        내가 접근을 잘못한 것도 있지만
        문제 티어에 비해 생각보다 너~~~~~~무 어려웠던 것 같음
    '''

    n = int(input())
    waters = list(map(int, input().split()))

    # n = 6
    # temp = '-2 -1 4 5 6 7'
    # waters = list(map(int, temp.split()))

    up_loc = bisect.bisect_left(waters, 0)

    # 음수 밖에 없을 때
    if up_loc == n:
        print(waters[-2], waters[-1])
        return
    
    # 양수 밖에 없을 때
    if up_loc == 0:
        print(waters[0], waters[1])
        return
    
    min_water = float('inf')

    answer_left = 0
    answer_right = 0

    for left_idx, left_water in enumerate(waters):

        # 양수는 이미 찾아봤으니 끝내기
        if left_water > 0:
            break

        # 양수인 숫자 중에서 나랑 최대한 가까운 숫자 찾기
        right = bisect.bisect_left(waters, left_water*-1)

        right_idx = right - 1

        # 왼쪽으로 탐색
        while left_idx < right_idx:

            now_water = abs(left_water + waters[right_idx])

            if min_water < now_water:
                break

            min_water = now_water
            answer_left = left_idx
            answer_right = right_idx

            right_idx -= 1

        # 오른쪽으로 탐색
        for right_idx in range(right, n):
            now_water = abs(left_water + waters[right_idx])

            if min_water < now_water:
                break

            min_water = now_water
            answer_left = left_idx
            answer_right = right_idx
        
        # 정답은 여러개일 수 있으므로 
        # 최소 값을 찾으면 끝내기
        if min_water == 0:
            break

    
    print(waters[answer_left], waters[answer_right])

    return

solution()


def firstSolu():

    '''
        다른 사람 풀이
        https://seongonion.tistory.com/100
        
        투 포인터를 사용한 풀이
        포인터를 이동시키는 기준만 알았다면 
        문제가 엄청 쉬워짐 ㅋㅋㅋㅋ
    '''
    
    n = int(input())
    liquids = list(map(int, input().split()))

    left_idx = 0
    right_idx = n - 1

    ans = abs(liquids[left_idx] + liquids[right_idx])
    ans_left = left_idx
    ans_right = right_idx

    while left_idx < right_idx:

        tmp = liquids[left_idx] + liquids[right_idx]

        if abs(tmp) < ans:
            ans_left = left_idx
            ans_right = right_idx

            ans = abs(tmp)

            if ans == 0:
                break
        
        # 그냥 현재 값이 음수냐 양수냐에 따라 이동시키면 됨... ㅋㅋㅋ
        if tmp < 0:
            left_idx += 1
        else:
            right_idx -= 1
    
    print(liquids[ans_left], liquids[ans_right])


def secondSolu():

    '''
        다른 사람 풀이 2
        https://seongonion.tistory.com/100

        이진 탐색을 사용한 풀이
        역시나 포인터를 이동시키는 기준을 알면 쉽게 풀 수 있음..
    '''

    n = int(input())
    liquids = list(map(int, input().split()))

    ans = float("INF")
    ans_left = 0
    ans_right = 0


    for i in range(n-1):
        current = liquids[i]

        start = i + 1
        end = n - 1

        # 내 뒤의 숫자들로 이진 탐색
        # 찾은 값과 더해서 음수면 오른쪽, 양수면 왼쪽으로 범위 줄여가기
        while start <= end:
            mid = (start + end) // 2
            tmp = current + liquids[mid]

            if abs(tmp) < ans:
                ans = abs(tmp)
                ans_left = i
                ans_right = mid

                if tmp == 0:
                    break
            
            if tmp < 0:
                start = mid + 1
            else:
                end = mid - 1
    
    print(liquids[ans_left], liquids[ans_right])