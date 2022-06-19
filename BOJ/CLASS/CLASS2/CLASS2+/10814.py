N = int(input())

i = 0

member_info = []
while i < N:

    age, name = input().split(' ')

    age = int(age)
    member_info.append([age, name])
    i += 1 

for info in sorted(member_info, key=lambda x:x[0]):
    print(info[0], info[1])