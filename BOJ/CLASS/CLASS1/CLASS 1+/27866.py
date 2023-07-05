
'''
    백준 27866. 문자와 문자열

    나의 풀이??
    그냥 문자랑 숫자 입력받고
    N번째 문자를 출력하면 되는 문제
'''

import sys
input = sys.stdin.readline

word = input()
idx = int(input())

print(word[idx-1])