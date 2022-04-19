# 문자열 압축 ㄷㄷ

def compressionWord(i, s, maxLength):
    if i == maxLength:
        return s

    comString = ''
    
    splitWordList = []
    index1= 0
    while index1 + i < maxLength:

        temp = ''
        for index2 in range(index1, index1+i):
            temp += s[index2]
        splitWordList.append(temp)
        index1 += i
    
    print(splitWordList)

    return ''


def solution(s):
    answer = 0
    
    stringLenght = len(s)

    lenghts = [9999] * (stringLenght+1)

    for i in range(1, stringLenght+1):
        processingStr = compressionWord(i, s, stringLenght)
        lenghts[i] = len(processingStr)


    return answer

print(solution("ababcdcdababcdcd"))