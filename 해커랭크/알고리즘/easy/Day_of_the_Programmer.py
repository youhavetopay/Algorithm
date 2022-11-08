## 그레고리력 이랑 율리우스력 해서 256번째 날 구하기

def dayOfProgrammer(year):
    # Write your code here
    
    julian = False
    
    days = [31, 28, 31,
            30, 31, 30,
            31, 31, 30,
            31, 30, 31
    ]
    
    if year <= 1918:
        julian = True
    
    leap_year = False
        
    if julian:
        if year % 4 == 0:
            leap_year = True
    else:
        if year % 4 == 0:
            leap_year = True
            if year % 100 == 0:
                leap_year = False
            if year % 400 == 0:
                leap_year = True
    
    sumDay = 0
    for index, day in enumerate(days):
        if leap_year and index == 1:
            sumDay += day + 1
        else:
            sumDay += day
            
        if sumDay >= 256:
            sumDay = 256 - (sumDay-day)
            
            yearStr = str(year)
            monthStr = index + 1
            if monthStr < 10:
                monthStr = '0' + str(monthStr)
            else:
                monthStr = str(monthStr)
            
            dayStr = sumDay
            if dayStr < 10:
                dayStr = '0' + str(dayStr)
            else:
                dayStr = str(dayStr)
            
            return dayStr + '.' + monthStr + '.' + yearStr

print(dayOfProgrammer(1918))