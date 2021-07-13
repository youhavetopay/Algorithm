# 균형잡힌 세상

while True:
    sentence = input()

    if sentence == '.':
        break

    stack = []

    flag = 0

    for word in sentence:
        if word == '[' or word == '(':
            stack.append(word)
        elif word == ']':
            if stack != [] and stack[-1] == '[':
                stack.pop()
            else:
                flag = 1
                break
        elif word == ')':
            if stack != [] and stack[-1] == '(':
                stack.pop()
            else:
                flag = 1
                break
    
    if stack != []:
        flag = 1
    
    if flag == 1:
        print('no')
    else:
        print('yes')