from collections import Counter

def solution(k, tangerine):

    '''
        나의 풀이
        사이즈 별로 귤이 주어질때
        임의로 K개를 선택할 때 사이즈 종류가 최소가 되는
        종류의 수를 구하는 문제

        나의 접근법
        일단 사이즈별로 귤들을 count하고
        처음엔 most_common을 사용했는데 시간초과 걸리길래
        그냥 size를 갯수를 기준으로 정렬해서 품
        아마 size 가지수가 엄청 많은 테스트케이스가 있는듯??

        그렇게 어려운 문제는 아니였음 ㅎㅎ
    '''
    
    answer = 0

    mandarin_counter = Counter(tangerine)

    sorted_size = sorted(list(mandarin_counter.keys()), reverse=True, key=lambda x:(mandarin_counter[x]))

    print(sorted_size)

    now_total_mandarin = 0
    while now_total_mandarin < k:
        count = mandarin_counter[sorted_size[answer]]
        now_total_mandarin += count
        answer += 1


    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))


def firstSolu(k, tangerine):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/138476/solution_groups?language=python3

        Count 한 다음에
        그냥 값을 기준으로 정렬해주면 됨 ㅋㅋㅋㅋㅋㅋㅋ
        나 뭐한거지? ㅋㅋㅋㅋㅋ
    
    '''

    answer = 0
    cnt = Counter(tangerine)

    for v in sorted(cnt.values(), reverse=True):
        k -= v
        answer += 1
        if k <= 0:
            break

    return answer