from collections import defaultdict

def solution(targets):

    '''
        나의 풀이(못품 ㅠㅠ)
        선의 시작점과 끝 지점들이 주어질 때
        모든 선을 관통하는 최소의 선의 개수를 구하는 문제

        나의 접근법(2 레벨 맞나..ㅜㅠㅜ)
        처음엔 그냥 시작부분을 기준으로 정렬해서 
        개수를 카운팅했는데 정답이 아니였음..

        그래서 누적합 응용?? 방식 처럼 시작점과 끝점을 
        기록하고 해볼려고 했었으나 여기서 어떻게 해야하는지 모르겠어서 포기..


        2레벨 맞나..
        2레벨은 잘 풀고 3레벨을 못풀어서 2레벨 모두 풀려고 했는데
        처음부터...ㅠㅠㅠㅠ
    '''

    answer = 1

    table = defaultdict(list)

    for start, end in targets:
        table[start + 0.1].append([True, end - 0.1])
        table[end - 0.1].append([False, start + 0.1])

    for key in sorted(table.keys()):
        print(key, table[key])
        

    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))

def firstSolu(targets):

    '''
        다른 사람 풀이
        https://velog.io/@mang0206/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9A%94%EA%B2%A9-%EC%8B%9C%EC%8A%A4%ED%85%9C-python

        아니... 이게 뭐야...
        나 너무 어렵게 생각했었나...ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
        풀이 너무 간단해서 더 어이없음 ㅠㅠㅠㅠㅠㅠㅠㅠㅠ

        그냥 정렬해서
        끝자리보다 높으면 해당 끝부분을 저장하면서 계속하면 됨...
        정렬 기준이 중요한듯...
        이 분 말로는 입출력 설명 그림을 보면 알 수 있다고 함....ㅠㅠㅠㅠ
    '''

    answer = 0
    targets.sort(key= lambda x: [x[1], x[0]])

    s = e = 0
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]
    
    return answer