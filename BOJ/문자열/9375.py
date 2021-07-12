test_case = int(input())

for _ in range(test_case):
    count = int(input())

    myCloth = {}

    for i in range(count):
        name, cate = map(str, input().split(' '))
        try:
            myCloth[cate].append(name)
        except KeyError:
            myCloth[cate] = [name]
    
    for key, value in myCloth.items():
        myCloth[key].append(len(value))
    
    