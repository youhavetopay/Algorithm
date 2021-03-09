def solution(mylist):
    answer = []
    
    for i in range(len(mylist)):
        answer.append(len(mylist[i]))
    return answer



#이게 파이썬 답게 ㅋㅋ
def solution(mylist):
    answer = []
    
    return list(map(len, mylist))
