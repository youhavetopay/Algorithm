def solution(record):
    answer = []
    
    
    userDict = {}
    
    orders = []
    
    for rec in record:
        info = list(map(str, rec.split(' ')))
        if len(info) == 3:
            userDict[info[1]] = info[2]
            orders.append([info[1], info[0]])
        else:
            orders.append([info[1], info[0]])
        
    for order in orders:
        if order[1] == 'Enter':
            answer.append(userDict[order[0]]+"님이 들어왔습니다.")
        elif order[1] == 'Leave':
            answer.append(userDict[order[0]]+"님이 나갔습니다.")
    
    return answer