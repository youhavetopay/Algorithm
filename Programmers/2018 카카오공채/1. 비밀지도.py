def solution(n, arr1, arr2):
    
    '''
        나의 풀이
        리스트의 숫자들을 2진수로 변환해서 or 연산 결과를
        #과 공백으로 나타내는 문제

        2018 카카오 공채 문제

        어렵지 않았음
        예전에 한번 풀어본 기억이 있어서 
        쉬웠음 ㅋㅋㅋㅋ

        예전에 풀어놓은거 보니까
        가관임 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        append대신에 insert(0)쓰고 ㅋㅋㅋㅋㅋㅋ
        아주 재밌게 풀어놓은듯 ㅋㅋㅋ
    '''


    answer = []

    for num1, num2 in zip(arr1, arr2):
        answer.append(bin(num1|num2)[2:].zfill(n))

    for idx, bin_num in enumerate(answer):

        change_code = ''
        for bin_code in bin_num:
            if bin_code == '1':
                change_code += '#'
            else:
                change_code += ' '

        answer[idx] = change_code

    return answer

print(solution(	6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))

def firstSoul(n, arr1, arr2):

    '''
        책 풀이
        비트연산을 사용하는게 중점인 문제였다고 함
        zfill, replace 를 통해 아주 파이썬 답게 풀어낸듯 함 ㅋㅋ
    '''

    maps = []
    for i in range(n):
        maps.append(
            bin(arr1[i] | arr2[i])[2:]
                .zfill(n)
                .replace('1', '#')
                .replace('0', ' ')

        )
    
    return maps