
'''
    백준 11054. 가장 긴 바이토닉 부분 수열
    수열에서 가장 긴 바이토닉 부분 수열을 구하는 문제

    바이토닉 수열
    증가하면서 중간에서 감소하거나
    증가 수열이거나
    감소 수열 인것 ㅋㅋㅋㅋㅋ
'''

import sys
input = sys.stdin.readline

import bisect

def find_increase_array(A, end_idx):

    LIS = [A[0]]

    for i in range(1, end_idx+1):

        if A[i] > LIS[-1]:
            LIS.append(A[i])
        else:
            LIS[bisect.bisect_left(LIS, A[i])] = A[i]
    
    print(LIS)
    return set(LIS)

def find_decrease_array(A, end_idx):

    LIS = [A[-1]]

    for i in range(len(A)-2, end_idx-1, -1):

        if A[i] > LIS[-1]:
            LIS.append(A[i])
        else:
            LIS[bisect.bisect_left(LIS, A[i])] = A[i]
    
    print(LIS)
    return set(LIS)

def solution():

    '''
        나의 풀이(나 혼자서 한건 아님..ㅋㅋ)

        나의 접근법
        순회를 하면서 각 해당 인덱스를 기준으로 
        왼쪽에서 증가하는 최장 증가수열 과 오른쪽으로 감소하는 최장 감소 수열의 길이를
        더해주는 방식으로 접근함

        근데 최장 증가 수열을 구하는걸 이상하게 해가지고 못 풀고
        자꾸 왜 틀리지 하다가
        
        결국 백준에서 최장 증가 수열 문제를 찾아서 해보면서
        내 코드의 틀린점을 찾아냄... ㅋㅋㅋㅋ
        최장 증가 수열 구하는 코드가

        LIS = [A[0]]

        for i in range(1, end_idx+1):

            if A[i] > LIS[-1]:
                LIS.append(A[i])
            else:
                LIS[bisect.bisect_left(LIS, A[i])] = A[i]
        
        print(LIS)

        인데

        LIS = [A[0]]

        for i in range(1, end_idx+1):

            if A[i] < LIS[-1]:
                LIS[bisect.bisect_left(LIS, A[i])] = A[i]
                
            else:
                LIS.append(A[i])
        
        print(LIS)

        이렇게 해가지고 틀렸다고 나왔던 거임 ㅋㅋㅋㅋ

        진짜... 이 문제 푼다고 거의 4시간 쓴듯...ㅋㅋㅋ
    '''

    # N = int(input())

    # A = list(map(int, input().split()))

    N = 5

    A = list(map(int, '178 91 593 601 77 33 733 774'.split()))


    max_bytonic_length = 0
    for idx in range(len(A)):

        incress = find_increase_array(A, idx)
        decress = find_decrease_array(A, idx)
        print(incress, decress, A[idx], idx)
        max_bytonic_length = max(len(incress) + len(decress) - 1, max_bytonic_length)


    print(max_bytonic_length)

    return

solution()


import sys
input = sys.stdin.readline

import bisect

N = int(input())
A = list(map(int, input().split()))

incress = find_increase_array(A, len(A)-1)

print(len(incress))


def firstSolu():

    '''
        다른 사람 풀이
        https://seohyun0120.tistory.com/entry/%EB%B0%B1%EC%A4%80-11054-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%B0%94%EC%9D%B4%ED%86%A0%EB%8B%89-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%92%80%EC%9D%B4

        최장 증가 수열을 구하는 방식이
        N^2 방법과 NlogN 이 있는데

        여기 방법은 N^2 으로 하는 풀이

        최장 증가 수열의 각 자릿수에 해당하는 길이와
        뒤집에서 최장 증가수열을 구하고

        각 자릿수에서 둘의 값을 더해주고 중복값 빼줘서 정답을 구하는 방식

    '''

    x = int(input())

    case = list(map(int, input().split()))

    increase = [1 for i in range(x)]

    for i in range(x):
        for j in range(i):
            if case[i] > case[j]:
                increase[i] = max(increase[i], increase[j]+1)

    decrease2 = [1 for i in range(x)]
    for i in range(x-1, -1, -1):
        for j in range(x-1, i, -1):
            if case[i] > case[j]:
                decrease2[i] = max(decrease2[i], decrease2[j]+1)

    result = [0 for i in range(x)]
    for i in range(x):
        result[i] = increase[i] + decrease2[i] -1 

    print(max(result))