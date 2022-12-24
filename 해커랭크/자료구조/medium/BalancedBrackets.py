def isBalanced(s):
    # Write your code here

    answer = 'YES'

    stack = []

    for word in s:
        if word == '{' or word == '[' or word == '(':
            stack.append(word)

        if word == '}':
            if len(stack) == 0:
                answer = 'NO'
                break
            
            if stack[-1] != '{':
                answer = 'NO'
                break
                
            stack.pop()
        
        if word == ']':
            if len(stack) == 0:
                answer = 'NO'
                break
            
            if stack[-1] != '[':
                answer = 'NO'
                break
                
            stack.pop()
        
        if word == ')':
            if len(stack) == 0:
                answer = 'NO'
                break
            
            if stack[-1] != '(':
                answer = 'NO'
                break
                
            stack.pop()


    if len(stack):
        answer = 'NO'

    return answer