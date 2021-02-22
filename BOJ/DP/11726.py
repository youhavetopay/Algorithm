value = int(input())

dp_list = [0 for i in range(value+1)]

dp_list[1] = 1
dp_list[2] = 2

for i in range(3, value+1):
    dp_list[i] = (dp_list[i-1] + dp_list[i-2]) % 10007

print(dp_list[value])


# n=int(input())
# a,b=1,1
# for i in range(n):a,b=b,a+b  ㄷㄷ
# print(a%10007) 