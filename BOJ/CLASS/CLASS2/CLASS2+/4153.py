# 직각삼각형 판별하는 문제

# 피타고라스 정리 사용하면 끝

number_list = [1,1,1]

while True:
    number_list = list(map(int, input().split(' ')))

    number_list.sort()

    if not all(number_list):
        break

    if (number_list[0]**2) + (number_list[1]**2) == (number_list[2]**2):
        print('right')
    else:
        print('wrong')