from collections import Counter

def get_combination_count(n):
    count = (n * (n - 1)) / 2
    return int(count)


def solution(weights):

    '''
        나의 풀이
        시소의 축과의 거리와 무게의 곱이 같으면 시소가 균형을 이루는데
        균형을 이루는 숫자들의 쌍을 구하는 문제

        처음엔 단순히 2중 for 문으로 해봤는데 당연히 시간초과...
        심지어 같은 무게가 여러개 있을 수 있어서 좀 고민좀 해봤음
        
        그래서 생각한 방법이
        Counter로 중복을 일단 제거 한 다음
        숫자 쌍과 해당 쌍의 개수를 set에 담아서 중복을 제거하는 방식으로 품

        생각보다??? 어려웠음 ㅋㅋㅋㅋ
        조합 수를 구하는걸 몰라서 ㅋㅋㅋㅋㅋ 검색해서 암 ㅋㅋㅋ
        실전이였으면 못풀었을듯.... 으이구
        수학이 너무 약한듯..
    '''

    answer = 0
    answers = set()

    # 거리 쌍
    dists = [
        [2, 3], [3, 2], [2, 4], [4, 2],
        [3, 4], [4, 3]
    ]

    weights_counter = Counter(weights)

    for key, value in weights_counter.items():

        # 같은 숫자가 여러개인 경우
        if value > 1:
            # 조합 개수 게산해서 넣어줌
            answers.add((key, key, get_combination_count(value)))
        
        # 거리에 따른 숫자 쌍 구하기
        for d_left, d_right in dists:
        
            now = key * d_left
            target = now / d_right

            # 반대편 무게가 있는지 검색
            if target == int(target) and int(target) in weights_counter:
                target = int(target)

                # 있으면 순서쌍 정렬해서 넣어주기
                if key < target:
                    answers.add((key, target, value * weights_counter[target]))
                else:
                    answers.add((target, key, value * weights_counter[target]))


    # 모든 순서쌍 더해주기
    for left, right, count in answers:
        answer += count

    return answer

print(solution([100,180,360,100,270]))


from collections import defaultdict

def firstSolu(weights):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/152996/solution_groups?language=python3

        이게 뭐야....
        정확한 원리는 이해가 안가긴 하지만
        얼추 나랑 비슷한거 같은데 원리가 좀 다른듯??
        비슷한 점은 dict에 담아서 현재 무게에서 가능한 무게들을 찾는 정도??
    '''

    answer = 0

    # 무게들 저장??
    dict1 = defaultdict(int)

    # 같은 숫자 Count 하는 곳??
    w_dict = defaultdict(int)

    for i in weights:
        # 현재 무게에 따른 반대편 무게들의 총 개수 구하기?
        tmp = dict1[i*2] + dict1[i*3] + dict1[i*4]

        # 균형을 이루는 무게가 하나라도 있고
        # 현재 무게랑 같은 무게가 있다면
        # 무게 조합 빼주기???
        if tmp != 0 and i in w_dict:
            tmp -= 2 * w_dict[i]
        
        # 현재 무게의 무게 경우의 수 넣어주기?
        for j in range(2, 5):
            dict1[i*j] += 1
        
        # 숫자 Count
        w_dict[i] += 1
        answer += tmp
    
    return answer