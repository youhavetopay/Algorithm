def solution (id_list, report , k):

    new_report = []
    for i in report:
        if i not in new_report:
            new_report.append(i)
    
    for order in new_report:
        report2 = order.split(' ')
        print(report2[1])
    
    
    return report2

id1 = ["muzi", "frodo", "apeach", "neo"]
re1 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k1 = 2

id2 = ["con", "ryan"]
re2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3

print(solution(id1, re1, k1))