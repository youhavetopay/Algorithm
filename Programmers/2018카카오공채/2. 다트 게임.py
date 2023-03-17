def solution(dartResult):

    '''
        나의 풀이
        문자열을 파싱해서 점수를 계산하는 문제

        역시 예전에 풀었던?? 문제이긴 하지만
        좀더 깔끔??? 하게 풀어봄 ㅋㅋㅋ

        획득한 점수를 리스트에 저장을 하고 
        문자를 하나하나 체크해가면서 점수를 구하는 방식으로 구현함

        구현 문제라서 어렵지는 않았음
    '''

    i = 0
    get_score = ''
    last_scores = []
    now_score = 0

    while i < len(dartResult):

        if dartResult[i].isdigit():
            get_score += dartResult[i]
            i += 1
        else:
            if now_score != 0:
                last_scores.append(now_score)

            now_score = int(get_score)
            get_score = ''

            while i < len(dartResult) and not dartResult[i].isdigit():
                if dartResult[i] == 'D':
                    now_score **= 2
                elif dartResult[i] == 'T':
                    now_score **= 3
                elif dartResult[i] == '*':
                    if last_scores != []:
                        last_scores[-1] *= 2
                    now_score *= 2    
                    
                elif dartResult[i] == '#':
                    now_score *= -1

                i += 1

    last_scores.append(now_score)

    return sum(last_scores)


print(solution("1D2S#10S"))

def firstSoul(dartResult):

    '''
        책 풀이
        리스트에 숫자를 저장해가면서 문자열을 파싱함
        역시 풀이가 엄청 깔끔함 ㅋㅋㅋ
    '''

    nums = [0]

    for s in dartResult:

        # 만약 보너스 관련이라면 최근 값에 처리를 해주고
        # 0을 넣어줌 -> 다음 점수
        if s == 'S':
            nums[-1] **= 1
            nums.append(0)
        elif s == 'D':
            nums[-1] **= 2
            nums.append(0)
        elif s == 'T':
            nums[-1] **= 3
            nums.append(0)
        
        # 옵션인 경우
        # 이미 0이 들어간 상태이니
        # 전전 값에 처리를 하고
        # 만약 전전전 값이 있으면 거기에도 처리하기
        elif s == '*':
            nums[-2] *= 2
            if len(nums) > 2:
                nums[-3] *= 2
        elif s == '#':
            nums[-2] *= -1
        
        else:
            # 만약 숫자라면 10의 자리수가 올수 있으니
            # 곱하기 10해주기 -> 점수는 0 ~ 10 사이
            nums[-1] = nums[-1] * 10 + int(s)
    
    return sum(nums)