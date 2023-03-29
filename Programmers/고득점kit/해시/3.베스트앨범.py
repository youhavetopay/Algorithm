import collections

def solution(genres, plays):

    '''
        나의 풀이
        일정 기준에 따른 번호 정렬 문제

        문제에 나와있는 테스트케이스가 적어서
        내 코드의 오류를 찾는데 조금 힘들었음 ㅋㅋ

        레벨 3이라는 것에 비해
        문제 자체도 그렇게....???? 어렵진 않았음 

        근데 이정도면 해시 문제가 아니고
        정렬문제 아님? ㅋㅋㅋㅋㅋ
    '''

    answer = []

    genres_types = collections.defaultdict(list)

    # 장르별로 번호랑 재생된 횟수를 넣음
    for idx, [genre, count] in enumerate(zip(genres, plays)):
        genres_types[genre].append([idx, count])
        # 넣고 나서 재생된 횟수를 기준으로 정렬 같다면 번호 작은게 먼저
        genres_types[genre].sort(reverse=True, key=lambda x:(x[1], -x[0]))

    # 장르별 총 재생 횟수를 구함
    sort_by_genre = []
    for key, values in genres_types.items():
        sort_by_genre.append([key, sum([count for _, count in values])])

    # 재생횟수를 기준으로 내림차순 정렬
    sort_by_genre.sort(reverse=True, key= lambda x:x[1])
    
    for genre, _ in sort_by_genre:

        # 장르별 최대 2곡만 가능하니 2개만 넣기
        count = 0
        for number, __ in genres_types[genre]:
            answer.append(number)
            count += 1
            if count == 2:
                break

    return answer


print(solution( ["classic", "Newage", "pop", "classic", "classic", "pop", "Newage"], [500, 1700, 600, 150, 800, 2500, 1500] ))


def firstSoul(genres, plays):

    '''
        다른 사람 풀이
        https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL3-%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%95%A8%EB%B2%94-Python

        나랑 전체적인 풀이 방법은 같음
        장르별로 모으고 장르별 재생 횟수를 같이 카운팅하는게 조금 차이점??
        그리고 슬라이싱 해서 2개만 뽑는게 코드 보기에는 훨씬 보기 좋은듯
    '''
    
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
    

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    
    return answer
