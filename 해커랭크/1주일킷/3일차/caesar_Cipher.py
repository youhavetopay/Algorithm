def caesarCipher(s, k):
    # Write your code here
    # a97  z122  A65  Z90
    answer = ''
    
    for word in s:
        if word.isalpha():
            wordNum = ord(word)
            if word.islower():
                if wordNum + k <= 122:
                    answer += chr(wordNum + k)
                else:
                    count = 0
                    while count < k:
                        wordNum += 1
                        count += 1
                        if wordNum > 122:
                            wordNum = 97
            
                    answer += chr(wordNum)
            else:
                if wordNum + k <= 90:
                    answer += chr(wordNum + k)
                else:
                    count = 0
                    while count < k:
                        wordNum += 1
                        count += 1
                        if wordNum > 90:
                            wordNum = 65
            
                    answer += chr(wordNum)
        else:
            answer += word           
    
    return answer


print(caesarCipher('www.abc.xy', 87))