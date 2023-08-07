
'''
    백준 120228. 평균은 넘겠지

    평균이 넘는 비율을 구하는 문제
'''

import sys
inout = sys.stdin.readline

'''
    나의 풀이

    재체점 때문에 틀렸다고 되어 있길래 다시 풀어봄
    찾아보니까 반올림에 대해 뭔가 수정이 있었던 것 같은데
    이거 때문에 테스트케이스 추가하니까 절반 이상이 틀렸습니다 라고 변경되었다고 함 ㅋㅋㅋㅋㅋㅋㅋ

    그래서 스페셜 저지로 넘어가면서 변경되었는듯?? ㅋㅋㅋㅋ
    그래도 일단 이 코드로는 통과함 ㅋㅋㅋ
'''

def solution():
    T = int(input())

    for _ in range(T):

        scores = list(map(int, input().split()))

        avg = (sum(scores) - scores[0]) / scores[0]

        over_count = 0
        for i in range(1, len(scores)):
            if scores[i] > avg:
                over_count += 1
        
        print("{:.3f}%".format(round((over_count / scores[0]) * 100, 3)))