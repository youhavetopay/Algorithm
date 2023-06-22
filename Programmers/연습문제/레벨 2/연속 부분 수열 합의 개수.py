def solution(elements):

    '''
        나의 풀이
        원형으로 이루어진 숫자 리스트가 있을때
        연속된 부분 수열의 합이 중복되지 않게 총 몇개가 있는지
        계산하는 문제

        나의 접근법
        데이터 길이가 최대 1000개 라서 그냥 완전탐색 해도 될 것 같기도해서???
        완전탐색으로 하니까 풀림
        계산하기 편하도록 리스트의 길이를 두배로 늘리고
        현재 길이에서 나올 수 있는 합을 계산해서 set에 넣어주는 방식으로 품

        솔직히 한번에 통과할 줄은 몰랐다 ㅋㅋㅋㅋ
        대신 조금 아슬아슬 했음 ㅋㅋ 최대 7000ms ㅋㅋㅋ
    '''

    total = set()
    new_elem = elements * 2
    
    now_length = 1
    while now_length <= len(elements):

        for i in range(len(new_elem) - now_length):
            now_seleted = new_elem[i:i+now_length]

            total.add(sum(now_seleted))

        now_length += 1

    return len(total)

print(solution([7,9,1,1,4]))


def firstSolu(elements):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/131701/solution_groups?language=python3

        이분도 완전탐색으로 했는데 훨씬 효율적임
        나는 리스트 슬라이스로 구해서 해당 리스트의 sum을 다시 구해줬어야 했는데
        이분은 현재 기본값에서 하나씩 더해가면서 체크해줌
        그래서 그런지 나보다 한 10배는 빠른듯 ㅋㅋㅋㅋ
    
    '''
    
    ll = len(elements)
    res = set()

    # 처음부터 마지막 원소까지
    for i in range(ll):
        ssum = elements[i] # 현재 기준값
        res.add(ssum)

        # 길이별로 넣어주기
        for j in range(i + 1, i + ll):
            ssum += elements[j % ll] # 기준값에 연속된 값들 더해주기
            res.add(ssum)
    
    return len(res)