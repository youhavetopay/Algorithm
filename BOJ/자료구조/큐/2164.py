# 카드2

num = int(input())

cardList = [x for x in range(1, num+1)]

while num > 1:
    del cardList[0]
    frontValue = cardList[0]
    del cardList[0]
    cardList.append(frontValue)
    num -= 1

print(cardList[0])