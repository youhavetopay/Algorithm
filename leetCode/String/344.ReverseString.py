# 344.Reverse String
# 난이도 : ★
# 문자열 뒤집기

# 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 
# 리턴 없이 리스트의 내부를 조작해라

from typing import List

def reverseString(s: List[str]) -> None: # 내가 한 풀이
    
    s = s[::-1] # 이거는 리트코드에서 오류남 -> 공간복잡도 제약이 있음 O(1)



def reverseString(s: List[str]) -> None: # 풀이 1, 2 (파이썬 풀이)
    
    s.reverse()

    s[:] = s[::-1]

def reverseString(s: List[str]) -> None: # 풀이 3 투포인터 사용
    
    left, right = 0, len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

    return s

print(reverseString(['1', '2', '3', '4', '5', '6']))
        