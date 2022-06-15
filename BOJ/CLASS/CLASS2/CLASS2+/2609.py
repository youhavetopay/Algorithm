# 두수의 최소공배수와 최대공약수 구하는 문제

# 그냥 반복문으로 풀어도 풀림

# 유클리드 호제법으로 하면 더빨리 찾음

'''
유클리드 호제법
a, b에 대해 a를 b로 나눈 r으로
a, b의 최대공약수 =  b와 r의 최대공약수

최대 공약수 = 유클리드 호제법
최소 공배수 = 두수의 곱 / 최대공약수
'''


A, B = input().split(' ')

A = int(A)
B = int(B)

max_num = 0
min_num = 0


for i in range(1, max(A,B)+1):
    if A % i == 0 and B % i == 0:
        max_num = i

A_List = []
B_List = []

count = 0
while True:
    count += 1

    now_A = A * count
    now_B = B * count

    A_List.append(now_A)
    B_List.append(now_B)

    if now_B in A_List:
        min_num = now_B
        break

    if now_A in B_List:
        min_num = now_A
        break

print(max_num)
print(min_num)


def findMinNumber(a, b):  # 유클리드 호제법
    r = a % b
    if r == 0:
        return b
    return findMinNumber(b, r)

print(findMinNumber(24, 18))
