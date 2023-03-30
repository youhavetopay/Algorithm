def solution(arr):

    '''
        나의 풀이
        숫자 리스트의 연속된 숫자를 제거하고 하나만 남겨두는 문제

        처음엔 단순히 중복만 제거하면 되는 줄 알았는데
        연속된 숫자를 남겨야해서
        그냥 이전에 담은거랑 다르면 넣고 아니면 
        넘어가는 방식으로 구현함

        문제만 이해하면 어렵지 않은 문제였음..
    '''

    answer = []
    
    for num in arr:
        if answer == []:
            answer.append(num)
            continue

        if answer and answer[-1] != num:
            answer.append(num)

    return answer

def firstSoul(arr):

    '''
        다른 사람 풀이
        https://velog.io/@joygoround/test-%EA%B0%99%EC%9D%80-%EC%88%AB%EC%9E%90%EB%8A%94-%EC%8B%AB%EC%96%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC

        풀이는 나랑 거의 똑같은데
        그냥 if문 조건이 조금 다름
    '''

    a = []

    for i in arr:
        if a[-1:] == [i]: continue

        a.append(i)
    
    return a