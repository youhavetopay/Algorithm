def solution(numbers):

    '''
        나의 풀이
        숫자 리스트가 주어질때 
        자기보다 큰 수를 오른쪽에서 찾는 문제

        나의 접근법
        데이터 크기가 최대 100만이라서 스택을 활용해야겠다는 생각을 함?? ㅋㅋ
        이제 이런문제 보면 무조건 스택부터 떠올려서 푸는데 안좋은 습관인가..?? ㅋㅋㅋ
        
        해당 인덱스와 숫자값을 스택에 담으면서 스택의 top보다 큰 수가 나오면 
        answer 에 해당 인덱스에 큰 수를 넣어주는 방식으로 구현
        그 후 반복문이 끝나고 스택에 여전히 값이 남아있으면 자기보다 큰 수가 오른쪽에 없다는 소리이니
        하나씩 빼면서 해당 인덱스에 넣어주는 방식으로 구현함

        처음 회사에서 문제 봤을떄는 좀 어려웠는데
        집에와서 해보니 생각보다 간단히?? 풀려서 신기했음 ㅋㅋ
        집에서 잘풀리나?? ㅋㅋㅋㅋ
    '''

    answer = [0] * len(numbers)
    stack = [[0, numbers[0]]]

    for i in range(1, len(numbers)):

        while stack and stack[-1][1] < numbers[i]:
            
            pop_idx, _ = stack.pop()
            answer[pop_idx] = numbers[i]

        stack.append([i, numbers[i]])
        print(stack, answer, i)


    while stack:
        i, _ = stack.pop()
        answer[i] = -1

    return answer

print(solution([9, 1, 5, 3, 6, 2]))

[2, 3, 3, 5]

[9, 1, 5, 3, 6, 2]


def firstSolu(numbers):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        접근법은 거의 똑같음

        에초에 -1로 초기화 하고
        스택에는 인덱스만 저장해두면 훨씬 코드가 간결해짐 ㅋㅋㅋㅋㅋㅋㅋㅋ
        자꾸 리스트에 뭔가 저장을 할때 인덱스랑 값 자체를 같이 저장하는 습관이 있는듯
        인덱스로 하면 리스트의 값에 접근할 수 있는걸 명심하자..!!!!
    '''

    stack = []
    result = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]
        
        stack.append(i)
    
    return result
