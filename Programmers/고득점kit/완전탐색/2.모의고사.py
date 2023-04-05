def solution(answers):

    '''
        나의 풀이
        일정 패턴으로 문제를 찍는 사람들 중
        가장 정답이 많은 사람을 찾는 문제

        그냥 패턴을 미리 저장하고
        이를 하나하나 체크하는 방식으로 품

        코드가 길긴 긴데 그렇게 어렵진 않았음 ㅋㅋ
    '''

    # 수포자가 찍는 정답 패턴
    soopo_answers = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    # 각각의 정답 패턴 index, 정답 개수, 번호
    soopo_counter = [
        [0, 0, 1],
        [0, 0, 2],
        [0, 0, 3]
    ]

    for answer in answers:

        for i in range(len(soopo_counter)):
            
            # 정답일 때
            if soopo_answers[i][soopo_counter[i][0]] == answer:
                soopo_counter[i][1] += 1
            
            # 다음 정답 index
            soopo_counter[i][0] = (soopo_counter[i][0] + 1) % len(soopo_answers[i])

    
    # 정답개수를 기준으로 정렬
    soopo_counter.sort(reverse=True, key=lambda x:(x[1]))
    print(soopo_counter)

    # 맨 앞에 있는 사람은 무조건 제일 많이 맞춘 사람
    winners = [soopo_counter[0][2]]
    max_count = soopo_counter[0][1]

    # 정답 수가 같은 사람 넣어주기
    for i in range(1, len(soopo_counter)):
        if soopo_counter[i][1] == max_count:
            winners.append(soopo_counter[i][2])
        else:
            break

    # 번호 순으로 정렬
    return sorted(winners)

print(solution([1, 3, 2, 4, 2]))


def firstSoul(answers):

    '''
        다른 사람 풀이
        https://it-garden.tistory.com/197

        나랑 똑같이 패턴을 미리 저장한건 같지만
        패턴 index에 접근하는 방법이랑
        정답을 만드는 과정에서 훨씬 효율적임
    '''

    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1
    
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
        
    return result