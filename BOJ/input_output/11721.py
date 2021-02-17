value = input()

count = 10

if count >= len(value):
    print(value)
else:
    for x in range(0, len(value), 10):
        print(value[x:count+x])
