num = int(input().strip())

answer = 65

if not num:
    answer = 97

for i in range(26):
    print(chr(i+answer), end='')


# 답
import string 
# 상수로 미리 지정해둔거라 빠름??
# string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
# string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits # 숫자 0123456789
print()
if num:
    print(string.ascii_uppercase)
else:
    print(string.ascii_lowercase)