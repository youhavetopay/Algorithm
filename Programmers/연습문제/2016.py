def solution(a, b):
    

    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = ['THU', 'FRI', 'SAT', 'SUN','MON','TUE','WED']

    totalDay = b

    for i in range(a-1):
        print(totalDay)
        totalDay += months[i]

   

    return days[totalDay%7]

print(solution(2,1))