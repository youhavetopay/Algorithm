
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

    # 문자열 만들기
    words = {chr(65 + i) : i for i in range(26)}

    # 현재 단어
    now_word = ['A'] * len(name)

    cursor = 0

    # 현재 커서가 가리키고 있는 단어
    cursor_word = now_word[cursor]
    cursor_word_idx = words[cursor_word]

    # 목표 단어
    target_word = name[cursor]
    target_word_idx = words[target_word]

    # 해당 단어로 가는 최단 경로 찾기
    if name[0] != now_word[0]:
        # 정방향이랑 역방향 중 거리 짧은 걸로
        answer += min(26 - target_word_idx + cursor_word_idx, abs(target_word_idx - cursor_word_idx))
        now_word[0] = name[0]

    # 단어를 완성하는 최소 입력 횟수
    min_push = [float('inf')]
    def dfs(now_words, cursor, push_count):

        # 현재까지 입력한 단어가 목표 단어인 경우
        if check_word(now_words, name):
            min_push[0] = min(push_count, min_push[0])
            return

        left = 1
        right = 1

        # 역방향으로 완성하지 못한 단어 위치 찾기
        left_i = cursor - 1
        while left_i != cursor:
            if now_word[left_i] != name[left_i]:
                break
            
            left_i -= 1
            left += 1
        
        # 커서를 이동 후 입력해야하는 단어의 위치 찾고 더해주기
        new_cursor = left_i
        new_push_count = push_count + left
        cursor_word = now_word[new_cursor]
        cursor_word_idx = words[cursor_word]

        target_word = name[new_cursor]
        target_word_idx = words[target_word]

        new_push_count += min(26 - target_word_idx + cursor_word_idx, abs(target_word_idx - cursor_word_idx))
        now_word[new_cursor] = name[new_cursor]

        # DFS
        dfs(now_words, new_cursor, new_push_count)

        # 해당 단어 원래대로 돌리고 정방향으로 완성하지 못한 단어 찾기
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

    # 최소값 반환
    return min_push[0]

def check_word(now_word, name):
    if ''.join(now_word) == name:
        return True
    
    return False

print(solution("JAN"))



def firstSolu(name):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/42860/solution_groups?language=python3

        처음에 목표 단어를 만드는데
        필요한 커서의 이동횟수를 먼저 구하고

        완성해야하는 단어의 위치를 
        왼쪽으로 가는거, 오른쪽으로 가는 거을 비교해서
        최소의 길이를 찾는 방식인듯??

        일단 알파벳 단어 만드는 커서 이동횟수 구하는 것 부터
        완성하지 못한 단어의 위치를 찾는 것 까지
        너무 깔끔함 ㅋㅋㅋㅋ

        아직 완벽히 이해는 못했지만
        참 그리디 하게 하신듯? ㅋㅋㅋㅋ

        난 완전탐색으로 했는데...
    '''

    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1

    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)
    
    answer += move
    return answer