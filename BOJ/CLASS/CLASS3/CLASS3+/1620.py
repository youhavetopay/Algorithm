import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

poketmon_number_dict = {}
poketmon_name_dict = {}

for i in range(1, N+1):
    name = input()
    name = name[:-1]
    poketmon_number_dict[i] = name
    poketmon_name_dict[name] = i


count = M
while count > 0:
    question = input()
    question = question[:-1]
    try:
        print(poketmon_name_dict[question])
    except:
        print(poketmon_number_dict[int(question)])
    
    count -= 1