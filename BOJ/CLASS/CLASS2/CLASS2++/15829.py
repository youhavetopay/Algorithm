# 백준 hashing 15829
# 문제가 좀 신기함 -> 부분 점수 기능이 있음

length = int(input())
words = input()

start_number = int(ord('a')) - 1

answer = 0

for idx, word in enumerate(words):
    answer += ((int(ord(word)) - start_number) * (31 ** idx))

print(answer % 1234567891)