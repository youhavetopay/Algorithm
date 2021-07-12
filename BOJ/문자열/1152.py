# 단어의 개수

word = input()

if word != ' ':
    wordList = list(word.strip().split(' '))

    print(len(wordList)) 

else:
    print(0) 