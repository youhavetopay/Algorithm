
'''
    프로그래머스 예상 대진표

    토너먼트 형식의 2^n 명으로 이루어진 참가자들이 있을 때

    번호 두개가 주어지면 이 둘이 만나는 라운드를 계산하는 문제
    (이 둘은 만나기 전까지 계속 이긴다고 가정)
'''

def solution(n,a,b):

    '''
        나의 풀이

        나의 접근법
        해당 번호가 홀수라면 +1 // 2를 하고
        짝수면 // 2 하는게 다음 라운드 번호라서
        둘의 차이가 1이 될때까지 반복하도록 했는데
        틀렸다고 나왔음 ㅋㅋㅋ

        그래서 질문하기를 통해서 반례를 봤는데
        4, 5 이렇게 있으면 나의 반복조건이 깨지는 걸 알아서
        조건으로 큰 수가 짝수가 되야하는 조건을 넣어주니 통과함 ㅋㅋ

        생각보다 쉽게 풀어서 기분 좋았음 ㅎㅎ
    '''

    answer = 1

    participant_A = a
    participant_B = b

    if a > b:
        participant_A = b
        participant_B = a

    while participant_B - participant_A != 1 \
        or participant_B % 2 != 0:

        if participant_B % 2 == 0:
            participant_B //= 2
        else:
            participant_B = (participant_B + 1) // 2
        
        if participant_A % 2 == 0:
            participant_A //= 2
        else:
            participant_A = (participant_A + 1) // 2
        
        answer += 1
        print(participant_A, participant_B)
    return answer


print(solution(100, 4, 5))


def firstSolu(n, a, b):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/12985/solution_groups?language=python3

        a, b 를 xor 취하는 과정에서 ab 사이의 거리가 가까우면 상위비트는 차이가 나지 않겠죠? 
        거꾸로 ab 사이의 거리가 멀면 상위비트가 차이 날 거고요. 
        그래서 xor 연산 결과의 길이를 리턴해주면 라운드가 나오는 아이디어인것으로 보여요.

        라고 함...

        xor 로 풀다니... 
        
    '''

    return ((a-1) ^ (b-1)).bit_length()