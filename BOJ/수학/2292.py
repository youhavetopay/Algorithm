# 벌집

number = int(input())

checkValue = 1
count = 1
sixValue = 6
while checkValue < number:
    sixValue = count * 6
    checkValue = checkValue + sixValue

    count += 1
    
print(count)