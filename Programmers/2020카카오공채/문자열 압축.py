def splitStringByLength(s, split_length):
    split_s = []

    s_length = len(s)

    for i in range(0, s_length, split_length):
        if i + split_length < s_length:
            split_s.append(s[i:i+split_length])
        else:
            split_s.append(s[i:])
    
    return split_s

def solution(s):

    '''
        나의 풀이
        문자열을 길이 별로 나누고 압축했을 때
        가장 길이가 작을때의 길이를 구하는 문제

        나의 접근법
        문자열을 1 ~ s의 길이까지 전부 나눠보고
        해당 문자열의 개수를 카운팅해서 넣는 방법으로
        가장 작은 길이를 찾아가는 방식으로 품

        2레벨 문제임에도 생각보다...?? 어려웠음 ㅋㅋ
        파이썬 슬라이스 기능 디게 편한듯 함 ㅋㅋㅋ
    '''

    answer = len(s)
    length = len(s)

    # 압축 단위 별로 체크하기
    for split_length in range(1, length):
        
        # 문자를 단위별로 나눠서 리스트로 만들기
        split_s = splitStringByLength(s, split_length)

        # 압축 문자 구하기
        compression_word = ''
        count = 1
        for i in range(1, len(split_s)):
            # 이전문자열이랑 같다면 횟수 올려주고
            if split_s[i-1] == split_s[i]:
                count += 1
            else:
                # 이전 문자열이랑 다르고
                # 중복 횟수가 2 이상이면 횟수랑 같이 넣어주기
                if count > 1:
                    compression_word += str(count) + split_s[i-1]
                else:
                    compression_word += split_s[i-1]
                
                count = 1

        # 반복문이 끝났을때 count 가 2 이상이라면 넣어주기
        if count > 1:
            compression_word += str(count) + split_s[-1]
        else:
            compression_word += split_s[-1]

        print(compression_word)

        # 가장 작은 길이 구하기
        answer = min(answer, len(compression_word))

    return answer

print(solution("ababcdcdababcdcd"))


def compress(text, tok_len):
    # 문자를 토큰의 길이별로 나누기 ㅋㅋ
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1

    # 압축하기
    # zip을 통해서 아~~~~~~~~~주 깔끔하게 함 ㅋㅋㅋ 대박 ㅋㅋ

    # 분리한 원본과 첫번째를 제외하고 뒤에 하나를 더 추가한 것을 
    # zip으로 하나씩 빼면서 i-1 이랑 i랑 비교함 ㅋㅋㅋ
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            # 압축 문자랑 반복 횟수를 리스트에 담기
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    
    # 반복 횟수가 2 이상인 사람만 횟수를 넣어줘서 길이를 계산
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def firstSolu(text):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        나랑 풀이법이 유사함
        대신 정말 파이써닉하게 풀어냈다는 점이 다른듯 ㅋㅋㅋㅋ
        그리고 불필요하게 모~~~든 길이별로 나누는게 아닌 절반까지만 나눠봄 -> 이게 맞지.. ㅋㅋㅋ

        문제 레벨이 낮을 수록 파이써닉한 풀이가 디게 많은듯 ㅋㅋ
    '''
    # 토큰 길이별로 문자열의 길이를 비교
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text/2) + 1)) + [len(text)]))