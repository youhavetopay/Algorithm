import itertools

def solution(relation):
    
    '''
        나의 풀이
        후보키 조합을 구하는 문제

        나의 접근법
        모든 키 조합을 구해서 중복을 제거하는 방식으로 품.. ㅋㅋ
        처음엔 쌩으로 DFS으로 조합구하다가 DFS의 DFS를 해야하는 사실을 알고
        그냥 itertools.combinations() 사용하는 걸로 변경함.. ㅋㅋㅋ

        레벨 2 라는것에 비해 생각보다 어려웠음 (1시간 30분??)
        그리고 질문하기에서 반례 못봤으면 아직도 못풀었을듯 ㅋㅋ

        그리고 range 할때 좀 실수좀 하지 말자 ㅡㅡ
    '''

    # 후보키 모음
    keys = set()
    
    # 인덱스들
    idxs = [ x for x in range(len(relation[0]))]

    # 최대 길이까지 조합 구하기
    for max_combi_length in range(1, len(relation[0])+1):
        
        # 해당 길이를 가지는 조합들 가져오기
        for combi in list(itertools.combinations(idxs, max_combi_length)):
            
            combi = list(combi)

            flag = False
            print(combi, 'pre')

            # 다시 조합 구하기 ex) 0, 1, 2 가 있을때 -> 0, 1  0,2  1,2 도 체크해야함
            for next_max_combi_length in range(1, max_combi_length):
                for next_combi in list(itertools.combinations(combi, next_max_combi_length)):
                    next_combi = list(next_combi)

                    # 만약에 해당 조합이 이미 후보키로 등록되었을 경우
                    # 끝내기
                    if ' '.join(map(str, next_combi)) in keys:
                        flag = True
                        break
                
                if flag:
                    break
            
            if flag:
                continue
            
            print(combi, 'aaaaaaa')

            # 유일하게 식별이 가능한지 -> 중복된 데이터가 없는지 체크
            check_data = []
            for i in range(len(relation)):
                temp = []
                for idx in combi:
                    temp.append(relation[i][idx])
                check_data.append(' '.join(map(str, temp)))
            
            if len(set(check_data)) == len(check_data):
                print(combi, 'add')
                keys.add(' '.join(map(str, combi)))



    # print(keys)
    print()
    print(keys)

    return len(keys)

#print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

# print(solution([
#     ["a","1","aaa","c","ng"],
#     ["a","1","bbb","e","g"],
#     ["c","1","aaa","d","ng"],
#     ["d","2","bbb","d","ng"]
# ]))

# print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))

#print(solution([["a","1","aaa","c","ng"],["a","1","bbb","e","g"],["c","1","aaa","d","ng"],["d","2","bbb","d","ng"]]))

print(solution([['a', 'aa'], ['aa', 'a'], ['a', 'a']]))

# [
#     ["a","1","aaa","c","ng"],
#     ["a","1","bbb","e","g"],
#     ["c","1","aaa","d","ng"],
#     ["d","2","bbb","d","ng"]
# ]



def firstSolu(relation):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/42890/solution_groups?language=python3

        비트연산으로 조합을 구함 -> 0000, 0001 이런식으로
        그리고 식별할 수 있는지 체크하는 방법

        비트연산으로 조합을 구하는게 신기해서 들고와봄 ㅎㅎ
        예~~~~~~전에 조합 구하는 방식에서 비트 연산으로 구하는 걸 본적있는데
        어려워서... ㅋㅋㅋ 포기했던 기억이 남 ㅋㅋㅋ
    '''

    answer_list = list()

    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()

        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            
            tmp_set.add(tmp)
        
        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            
            if not_duplicate:
                answer_list.append(i)
    
    return len(answer_list)