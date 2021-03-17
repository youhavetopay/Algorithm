def solution(mylist):
    answer = []
    
    for i in mylist:
        if i%2 == 0:
            answer.append(i**2)
    
    return answer


def solution2(mylist):
    answer = [i**2 for i in mylist if i%2==0]
    return answer

