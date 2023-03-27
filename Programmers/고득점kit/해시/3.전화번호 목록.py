def solution(phone_book):

    '''
        나의 풀이
        문자열 리스트 중에서 다른 문자의 접두어가 있는지 없는지
        확인하는 문제

        트라이 자료구조를 활용해서 품
        처음에 트라이 했는데도 몇개 틀려서
        살짝 고민했는데
        문자열 길이 순으로 정렬을 하니까 풀림 ㅎㅎ
        근데 효율성에서 살짝 아슬아슬했었음 ㅋㅋ
    '''

    book = {}

    # 길이 순으로 정렬
    # 안 그러면 일반 문자열을 넣고 접두어를 넣는 경우
    # 판별을 못함
    phone_book.sort(key=lambda x: len(x))

    for phone in phone_book:

        now_book = book
        for idx, num in enumerate(phone):

            # 해당 숫자가 없는 경우
            if num not in now_book:
                now_book[num] = {}
                now_book = now_book[num]

            else:
                # 해당 숫자가 있는 경우
                now_book = now_book[num]

                # 이전에 넣은 문자열의 마지막인 경우
                # 즉 접두어가 있는 경우
                if 'end' in now_book:
                    return False
                
            # 해당 숫자가 마지막인 경우 
            # 별도로 표시
            if idx == len(phone)-1:
                now_book['end'] = True
                
        
        print(book)

    # 접두어가 존재하지 않는 경우
    return True

print(solution(["55", "1231236679", "1195524421"]))


def firstSoul(phone_book):

    '''
        다른 사람 풀이
        (프로그래머스)

        문자열을 정렬을 하면 문자 순으로 정렬이 됨
        그렇게 해서 앞에꺼랑 뒤에꺼랑 자꾸 비교하면 됨 ㅋㅋㅋ

        이게 훨씬 빠르고 간결한듯???
    '''

    phone_book.sort()
    print(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        
        # startswith는 
        # p2의 시작 문자 즉 접두어가 p1 인지 체크하는 것
        if p2.startswith(p1):
            return False
        
    return True

print(firstSoul(["119", "97674223", "1195524421"]))