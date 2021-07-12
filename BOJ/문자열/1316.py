# 그룹 단어 체커

count = int(input())
answer = 0

for i in range(count):
    word = input()
    
    checkList = []
    lastWord = ''
    for tempWord in word:
        if tempWord not in checkList:
            checkList.append(tempWord)
            lastWord = tempWord
        elif lastWord == tempWord:
            continue
        else:
            break
    else:
        answer += 1

print(answer)

