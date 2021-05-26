# 숫자카드2

myCardcount  = input()

cardValue = list(map(int, input().split()))

myCard = {}

for card in cardValue:
    try:
        myCard[card] += 1
    except KeyError:
        myCard[card] = 1

input()
checkCards = list(map(int, input().split()))
answers = []

for card in checkCards:
    try:
        temp = myCard[card]
        answers.append(temp)
    except KeyError:
        answers.append(0)
    
for num in answers:
    print(num, end=" ")