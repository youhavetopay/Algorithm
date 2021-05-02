def solution(s):
    answer = 0
    if len(s)%2 == 0:

        for j in range(len(s)):
            stack = []
            checkValue = 1
            for i in range(len(s)):
                
                if s[i] == '{' or s[i] == '[' or s[i] == '(':
                    stack.append(s[i])
                else:
                    if len(stack) < 1:
                        checkValue = -1
                        break

                    if s[i] == '}':
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            checkValue = -1
                            break

                    if s[i] == ']':
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            checkValue = -1
                            break
                    
                    if s[i] == ')':
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            checkValue = -1
                            break
                
            if checkValue == 1:
                answer += 1
        
            tempStr1 = s[0]
            
            s = s[1:]

            s = s + tempStr1
            
        return answer

                
    else:
        return 0
    

list1 = "}]()[{"

print(solution(list1))
