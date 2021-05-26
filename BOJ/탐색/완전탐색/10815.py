# 숫자카드
# 도대체 뭐가 안된거지? ㅋㅋㅋㅋㅋ
import sys

myCardCount = int(sys.stdin.readline())

cardStr = sys.stdin.readline()

myCards = {}

for num in cardStr.split():
    myCards[num] = 1

answer = ''

checkCardCount = int(sys.stdin.readline())
checkStr = sys.stdin.readline()

for num in checkStr.split():
    try:
        temp = myCards[num]
        answer += ' 1'
    except KeyError:
        answer += ' 0'

print(answer[1:])