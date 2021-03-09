num, base = map(int, input().strip().split(' '))

str_num = str(num)[::-1]

answer = 0

for i in range(len(str_num)):
    print(int(str_num[i]), (base**i))
    answer += int(str_num[i])*(base**i)

print(answer)

#이게 답 ㅋㅋㅋ
print(int(str(num), base))  
