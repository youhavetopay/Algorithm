list2 = [['9',1]]
count =0
while True:
    list1 = []

    a = input()
    b= int(input())

    list1.append(a)
    list1.append(b)
    list2.append(list1)
    print(list2)
    count +=1
    if count > 2:
        break