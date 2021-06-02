# 숫자카드

def countList(cards):
    
    count = {}

    for card in cards:
        try:
            count[int(card)] += 1
        except KeyError:
            count[int(card)] = 1

    return count

def findValue(countingList):
    
    answerLoc = -1
    answerValue = -1

    for index, value in countingList.items():
        if answerValue < value:
            answerValue = value
            answerLoc = index

        elif answerLoc < index and answerValue == value:
            answerLoc = index
    
    return answerLoc, answerValue

T = int(input())

for test_case in range(1, T + 1):
    cardCount = int(input())

    cards = input()

    countedList = countList(cards)

    answerLoc, answerValue = findValue(countedList)

    print('#'+str(test_case), answerLoc, answerValue)