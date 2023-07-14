
'''
    프로그래머스 조이스틱

    조이스틱을 조작해 목표 문자열을 만들때
    최소로 눌러야 하는 횟수를 구하는 문제
'''

import sys

sys.setrecursionlimit(2_000_000)

def solution(name):

    '''
        나의 풀이

        나의 접근법
        완전탐색으로 품
        솔직히 문제 유형 바꿔야 함 ㅡㅡ
        그리디가 아니라 완전탐색으로 ㅡㅡ

        처음엔 그리디하게
        왼쪽과 오른쪽에서 완성이 안된 문자가 있는 위치를 찾고
        더 가까운 곳으로 이동해서 했는데 틀렸다고 나옴...

        그래서 어떤 경우가 틀리는지 잘모르겠어서
        질문하기에서 반례를 보고 완전탐색으로 방향을 바꿈..

        왼쪽으로 가서 선택하는 경우, 
        오른쪽으로 가서 선택하는 경우 
        이렇게 두개로 나눠서
        DFS 방식으로 품 
    '''
    
    answer = 0

    words = {chr(65 + i) : i for i in range(26)}

    now_word = ['A'] * len(name)

    cursor = 0

    cursor_word = now_word[cursor]
    cursor_word_idx = words[cursor_word]

    target_word = name[cursor]
    target_word_idx = words[target_word]

    if name[0] != now_word[0]:
        answer += min(26 - target_word_idx + cursor_word_idx, abs(target_word_idx - cursor_word_idx))
        now_word[0] = name[0]

    min_push = [float('inf')]
    def dfs(now_words, cursor, push_count):

        if check_word(now_words, name):
            min_push[0] = min(push_count, min_push[0])
            return

        left = 1
        right = 1

        left_i = cursor - 1
        while left_i != cursor:
            if now_word[left_i] != name[left_i]:
                break
            
            left_i -= 1
            left += 1
        
        new_cursor = left_i
        new_push_count = push_count + left
        cursor_word = now_word[new_cursor]
        cursor_word_idx = words[cursor_word]

        target_word = name[new_cursor]
        target_word_idx = words[target_word]

        new_push_count += min(26 - target_word_idx + cursor_word_idx, abs(target_word_idx - cursor_word_idx))
        now_word[new_cursor] = name[new_cursor]
        dfs(now_words, new_cursor, new_push_count)
        now_word[new_cursor] = 'A'

        right_i = cursor + 1
        while right_i != cursor:
            if right_i >= len(name):
                right_i = 0

            if now_word[right_i] != name[right_i]:
                break
            
            right_i += 1
            
            right += 1

        new_cursor = right_i
        new_push_count = push_count + right
        cursor_word = now_word[new_cursor]
        cursor_word_idx = words[cursor_word]

        target_word = name[new_cursor]
        target_word_idx = words[target_word]

        new_push_count += min(26 - target_word_idx + cursor_word_idx, abs(target_word_idx - cursor_word_idx))
        now_word[new_cursor] = name[new_cursor]
        dfs(now_words, new_cursor, new_push_count)
        now_word[new_cursor] = 'A'

    dfs(now_word, cursor, answer)
    return min_push[0]

def check_word(now_word, name):
    if ''.join(now_word) == name:
        return True
    
    return False

print(solution("JAN"))