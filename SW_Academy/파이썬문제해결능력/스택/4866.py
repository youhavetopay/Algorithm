T = int(input())
# 조금 업그레이드 된 괄호 검사
for test_case in range(1, T+1):
    stack = []

    inputStr = input()
    answer = 1
    for word in inputStr:
        if word == "'" or word =='"':
            if word == stack[-1]:
                stack.pop()
            else:
                stack.append(word)
        elif stack != []:
        
            if stack[-1] == '"' or stack[-1] == "'":
                continue

        if word == '(' or word == '{' or word == '[':
            stack.append(word)
        
        elif word == ')':
            if  stack == [] or stack[-1] != '(':
                answer = 0
                break
            else:
                stack.pop()

        elif word == '}':
            if stack == [] or stack[-1] != '{':
                answer = 0
                break
            else:
                stack.pop()
        
        elif word == ']':
            if stack == [] or stack[-1] != '[':
                answer = 0
                break
            else:
                stack.pop()
        
    
    if answer == 0 or stack != []:
        print('#'+str(test_case), 0)
    else:
        print('#'+str(test_case), 1)
