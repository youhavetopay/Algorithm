import collections

def solution(gems):

    '''
        나의 풀이 (내힘으로 풀었다고 해야하나..? ㅋㅋ)
        문자열 리스트에서 모든 종류를 포함하고 있는 최소의 길이를 구하는 문제

        나의 접근법
        적당한?? 해석을 보고 푼거라서... 큰 의미는 없는듯...ㅜㅜ 효율성이 너무 어려움..

        먼저 set으로 종류의 개수를 구하고
        투포인터로 풀었음
        처음엔 right 먼저 전진시키면서 dict자료형에 해당 보석의 개수를 카운팅함
        그리고 dict의 key의 개수가 set의 길이랑 같다면
        left를 1씩 증가시키면서 dict에서 카운팅했던걸 빼줌 -> 최소의 길이를 찾기
        그렇게 찾았다면 해당 길이를 기록하고 해당 길이를 유지하면서 슬라이딩 윈도우를 해주는 방식으로 품..

        효율성이 진짜 너무 어려운듯..
        솔직히 힌트 못봤으면 아직도 못풀었을듯 함..
        에구..

    '''

    answer = []

    gem_kinds = set(gems)
    if len(gem_kinds) == 1:
        return [1, 1]

    now_gem = collections.defaultdict(int)

    left, right = 0, 1

    now_gem[gems[left]] += 1


    max_length = float('inf')


    while right < len(gems) and left < right:

        print(left, right, answer, now_gem)
        now_gem[gems[right]] += 1

        
        if len(now_gem.keys()) == len(gem_kinds):
            
            while now_gem[gems[left]] >= 2:
                now_gem[gems[left]] -= 1
                left += 1

            answer.append([left+1, right+1])

            max_length = min(max_length, right - left + 1)
        
        right += 1
        
        
        if max_length < right - left + 1:
            now_gem[gems[left]] -= 1
            if now_gem[gems[left]] == 0:
                del now_gem[gems[left]]
            left += 1
        
    print(answer)
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))

    return answer[0]

print(solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))


def firstSolu(gems):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        나랑 비슷하게 dict형에서 카운팅해서 투포인터 형식으로 했는데
        코드 자체는 훨씬 깔끔한듯 함 ㄷㄷ
    '''

    size = len(set(gems))

    # 첫번째꺼 카운팅 해주기
    dic = {gems[0]:1}

    # 정답 기록용
    temp = [0, len(gems) - 1]

    # 투 포인터
    start, end = 0, 0

    # 포인터가 최대 길이를 넘지 않을때 까지
    while start < len(gems) and end < len(gems):

        # 모든 보석을 가지고 있을때
        if len(dic) == size:
            # 해당 길이가 짧으면 정답 갱신하기
            if end - start < temp[1] - temp[0]:
                temp = [start, end]
            
            # start 앞으로 한칸 당기기
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            
            start += 1
        
        # 아직 모든 보석의 종류를 가지고 있지 않을 때
        else:
            # end 한칸 당기기
            end += 1
            if end == len(gems):
                break
            
            # 카운팅 해주기
            if gems[end] in dic.keys():
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1
    
    return [temp[0] + 1, temp[1] + 1]