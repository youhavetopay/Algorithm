def solution(s):

    '''
        나의 풀이
        문자열로된 숫자 영문을 숫자로 바꾸는 문제

        나의 접근법
        replace쓰면 쉽게 풀 수 있음 ㅋㅋ

        예전에 풀었을 때는 replace 안쓰고
        스택으로 직접 확인했는데
        replace가 참 편한듯 ㅋㅋㅋㅋ
    '''

    nums_str = [
        'zero', 'one', 'two', 'three',
        'four', 'five', 'six', 'seven',
        'eight', 'nine'
        ]

    for i, num in enumerate(nums_str):
        while num in s:
            s = s.replace(num, str(i))
    return int(s)

print(solution("one4seveneight"))


def firstSolu(s):
    
    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        깔끔하게 dict 자료형을 사용해서 품
        쉬운 문제라서 풀이가 거기서 거긴듯... ㅋㅋㅋ
    '''

    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)

    return answer