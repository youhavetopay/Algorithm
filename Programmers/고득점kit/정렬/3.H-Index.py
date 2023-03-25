def solution(citations):

    '''
        나의 풀이
        숫자리스트에서 N 보다 큰게 N개 이상이고 나머지는 N보다 작은
        최대 N을 찾는 문제

        좀 어렵고 비효율적으로 푼듯 ㅋㅋㅋㅋ
        문제 설명하려고 보니 이상하게 푼걸 께달음 ㅋㅋㅋㅋ
    '''

    answer = 0

    citations.sort() # 일단 정렬
    
    i = 0

    now_count = 0
    while i < len(citations):
        
        over_count = 0 # 나보다 같거나 큰 수의 개수
        down_count = 0 # 나보다 같거나 작은 수의 개수

        if citations[i] >= now_count: # 현재 수 비교

            # 정렬되어 있으므로 나의 앞에 있는 수는 전부 같거나 큰 수
            over_count = len(citations) - i
            down_count = i # 나 뒤에 있는 수는 같거나 작은 수

            # 현재 카운트가 문제의 조건을 만족할 경우
            if over_count >= now_count and now_count >= down_count:
                answer = now_count
            
            # 비교 수를 하나씩 올려가면서 체크
            now_count += 1
        else:
            i += 1
            continue
        


    return answer

print(solution([9, 7, 6, 2, 1]))

def firstSoul(citations):
    '''
        다른 사람 풀이
        https://yunaaaas.tistory.com/56

        내가 너무 이상하게 푸는 듯 ㅋㅋㅋㅋㅋㅋ
    '''

    # 정렬
    citations.sort()

    for idx , citation in enumerate(citations):

        # 현재 값보다 같거나 큰 수의 개수가
        # 현재 값보다 같거나 작을 때
        if citation >= len(citations) - idx :
            return len(citations) - idx
    return 0