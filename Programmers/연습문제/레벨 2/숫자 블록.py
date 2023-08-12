
'''
    프로그래머스 숫자 블록
    총 10억개의 블록 칸이 있고
    1 ~ 1천만 번호의 블록들을 각각 배수에 넣었을때
    일정 구간의 가장 최근에 들어간 블록이 뭔지 계산하는 문제
'''


def solution(begin, end):

    '''
        나의 풀이

        나의 접근법
        보니까 가장 최근 블록이 최대 약수이길래
        
        짝수면 절반, 홀수면 약수중 가장 큰수를 넣어줬는데
        효율성이 다 틀렸다고 나왔음 ㅋㅋㅋ

        그래서 질문하기를 봤는데
        블록의 최대 번호가 1천만인데 블록의 칸은 10억이라서
        1천만이 넘어가는 약수는 넣으면 안됐었음 ㅋㅋㅋ
        
        그래서 짝수, 홀수 상관 없이 1천만이 넘지 않는 최대 약수를 
        찾아서 넣어주니 풀렸음 ㅎㅎ
    '''

    answer = [0] * (end - begin + 1)

    idx = 0
    for i in range(begin, end+1):

        answer[idx] = find_max_measure(i)

        idx += 1
    
    if begin == 1:
        answer[0] = 0

    return answer

def find_max_measure(n):

    # 약수 구하는 알고리즘

    measuer = []

    # n의 제곱근까지 탐색
    for i in range(1, int((n ** (1/2)))+1):
        if n % i == 0 and i <= 10_000_000:
            measuer.append(i)
    
    # 구한 약수들로 다시 한번 나눠줘서 약수 구하기
    new_measuer = []
    for m in measuer:
        new_m = n // m
        if new_m <= 10_000_000:
            new_measuer.append(new_m)
    
    measuer += new_measuer
    measuer.sort()
    
    if measuer[-1] == n:
        measuer.pop()

    return measuer[-1]

print(solution(999_995_000, 1_000_000_000))



def find_max_measure(n):

    # 약수 구하는 알고리즘

    measuer = []

    # n의 제곱근까지 탐색
    for i in range(1, int((n ** (1/2)))+1):
        if n % i == 0:
            measuer.append(i)
    
    # 구한 약수들로 다시 한번 나눠줘서 약수 구하기
    new_measuer = []
    for m in measuer:
        new_measuer.append(n // m)
    
    measuer += new_measuer
    measuer.sort()

    return measuer