# 단어공부

word = input()

wordCount = {}

for i in word:
    try:
        wordCount[str(i).lower()]+= 1
    except KeyError:
        wordCount[str(i).lower()] = 1

maxList = []

maxValue = 0

for key, value in wordCount.items():
    if maxValue < value:
        maxValue = value
        maxList = [str(key)]
    elif maxValue == value:
        maxList.append(str(key))

if len(maxList) > 1:
    print('?')
else:
    print(maxList[0].upper())