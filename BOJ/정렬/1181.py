# 단어 정렬

import sys
from collections import defaultdict

input = sys.stdin.readline

wordCount = int(input())

words = defaultdict(list)

for i in range(wordCount):
    word = input().strip()
    length = len(word)
    if words[length] == None:
        words[length] = word
    else:
        if word not in words[length]:
            words[length].append(word)


for value in sorted(list(words.keys())):
    if len(words[value]) >1:
        for word in sorted(words[value]):
            print(word)
    else:
        print(words[value][0])