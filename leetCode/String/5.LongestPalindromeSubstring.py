# 5. Longest Palindrome Substring
# 가장 긴 팰린드롬 부분 문자열
# 난이도 : ★★


# 가장 긴 팰린드롬 부분 문자열을 출력하라.

def longestPalindrome(s: str) -> str: # 나의 풀이 조금 보고 했음
    answer = ''
    s_length = len(s)

    if s == s[::-1]:  # 문자 전체가 팰린드롬인 경우
        return s

    for i in range(s_length): # 완전탐색으로 품 -> 거의 아슬아슬하게 됨 9500ms ㅋㅋ
        for j in range(i+1, s_length+1):
            word_pice = s[i:j]
            if word_pice == word_pice[::-1]:
                if len(answer) < len(word_pice):
                    answer = word_pice
        

    return answer


s1 = "babad"
s2 = "cbbd"
s3 = 'abcd'
print(longestPalindrome(s1))

def longestPalindrome(s: str) -> str: # 첫번째 풀이 (나의 풀이보다 훨씬빠름 550ms정도?)

    if s == s[::-1]: # 전체가 팰린드롬일때 return
        return s


    # 팰린드롬인지 체크하는 함수
    # 투포인터 형식
    # 만약 팰린드롬이 맞다면 양옆으로 1칸씩 확장 후 해당 팰린드롬 문자 리턴
    def check_palindrome(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    answer = ''

    # 팰린드롬이 되는 문자를 찾기 위해 한칸씩 이동
    for i in range(len(s)-1):
        answer = max(
            answer
          , check_palindrome(i, i+1) # 문자갯수가 홀수인 팰린드롬 체크
          , check_palindrome(i, i+2) # 문자갯수가 짝수인 팰린드롬 체크
          , key=len # 길이가 가장 긴 문자를 리턴
        )

    return answer