

# 입력한 수에서 소수 찾기

# 에라토스테네스의 체 구현함
''' 
1. 숫자 배열 생성 2부터
2. 2 자신을 제외한 2의 배수를 제거
3. 제거 안된 3의 배수 제거 
4. 반복 
5. 남은 숫자는 전부 소수
'''

def deleteNotPrimeNumber(number_list, target_num):
    
    for idx, num in enumerate(number_list):
        if num != target_num and num % target_num == 0 and num != -1:
            number_list[idx] = -1
    
    return number_list

def makePrimeNumberList(max_number):
    
    number_list = [i for i in range(2, max_number+1)]

    for idx in range(len(number_list)):
        if number_list[idx] != -1:
            number_list = deleteNotPrimeNumber(number_list, number_list[idx])
    
    return number_list


number_length = int(input())

numbers = list(map(int, input().split(' ')))

prime_number_list = makePrimeNumberList(max(numbers))

answer = 0
for num in numbers:
    if num in prime_number_list:
        answer += 1

print(answer)