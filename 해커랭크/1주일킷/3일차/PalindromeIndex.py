def makeWordIndexs(word):
    left = 0
    right = len(word)-1

    word_indexs = []

    while left < right:

        if word[left] != word[right]:
            word_indexs.append([left, right])

        left += 1
        right -= 1
    
    return word_indexs

def palindromeIndex(s):
    # Write your code here

    word_indexs = makeWordIndexs(s)

    print(word_indexs)
    if len(word_indexs) == 0:
        return -1

    first_word_remove_s = s[0:word_indexs[0][0]] + s[word_indexs[0][0]+1:]
    last_word_remove_s = s[0:word_indexs[0][1]] + s[word_indexs[0][1]+1:]
    
    temp1 = makeWordIndexs(first_word_remove_s)
    temp2 = makeWordIndexs(last_word_remove_s)

    if len(temp1) == 0:
        return word_indexs[0][0]
    elif len(temp2) == 0:
        return word_indexs[0][1]

    return -1

s1 = 'quyjjdcgsvvsgcdjjyq'

print(palindromeIndex(s1))