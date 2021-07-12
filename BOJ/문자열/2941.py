# 크로아티아 알파벳

croatiaWordList = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

inputWord = input()

for croatiaWord in croatiaWordList:
    while croatiaWord in inputWord:
        inputWord = inputWord.replace(croatiaWord, 'a')

print(len(inputWord))