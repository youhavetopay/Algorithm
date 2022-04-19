# 125. Valid Palindrome
# 유효한 팰린드롬
# 난이도 : ★

# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며,
# 영문자와 숫자만을 대상으로 한다

# 팰린드롬 : 앞뒤가 똑같은 문자


# 내가 푼 코드
def isPalindrome(s: str) -> bool:

    answer = False

    new_word = ''

    for word in s:
        if word.isalpha():
            new_word += word.lower()
        if word.isdigit():
            new_word += word

    reverse_word = ''
    for i in range(len(new_word)-1, -1, -1):
        reverse_word += new_word[i]
    

    if new_word == reverse_word:
        answer = True

    return answer

print(isPalindrome("A man, a plan, a canal: Panama"))

def isPalindrome(s: str) -> bool: #첫번째
    strs = []

    for char in s:
        if char.isalnum(): # 문자 혹은 숫자인지 판별
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))


from collections import deque
def isPalindrome(s: str) -> bool:  #두번째 첫번째 풀이 최적화
    strs: Deque = deque() # 데크 사용

    for char in s:
        if char.isalnum(): # 문자 혹은 숫자인지 판별
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop(): # 데크의 popleft는 O(1)이라서 훨씬 빠름
            return False

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))

import re
def isPalindrome(s: str) -> bool:  # 세번째 풀이 슬라이싱 사용
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s) # 정규표현식으로 문자와 숫자만 가져오기

    return s == s[::-1] # 슬라이싱으로 뒤집기 ㄷㄷ 

print(isPalindrome("A man, a plan, a canal: Panama"))